import numpy as np

import pyglet
import gym
from gym import core, spaces
from gym.envs.registration import register
from gym.envs.classic_control import rendering

class Fourrooms(gym.Env):
    metadata = {'render.modes': ['human']}
    def __init__(self):
        layout = """\
wwwwwwwwwwwwwwwwwwwwwww
w     w     w         w
w     w     w         w
w                     w
w     w     w         w
w     w     w         w
wwwwwwwwwwwwwwwwwwwwwww
"""
#         layout = """\
# wwwwwwwwwwwww
# w     w     w
# w     w     w
# w           w
# w     w     w
# w     w     w
# ww wwww     w
# w     www www
# w     w     w
# w     w     w
# w           w
# w     w     w
# wwwwwwwwwwwww
# """
        self.occupancy = np.array([list(map(lambda c: 1 if c=='w' else 0, line)) for line in layout.splitlines()])

        # From any state the agent can perform one of four actions, up, down, left or right
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Discrete(np.sum(self.occupancy == 0))

        self.directions = [np.array((1,0)), np.array((0,1)), np.array((-1,0)), np.array((0,-1))]
        self.rng = np.random.RandomState(1234)

        self.tostate = {}
        statenum = 0
        height = self.occupancy.shape[0]
        width = self.occupancy.shape[1]
        for i in range(height):
            for j in range(width):
                if self.occupancy[i, j] == 0:
                    self.tostate[(i,j)] = statenum
                    statenum += 1
        self.tocell = {v:k for k,v in self.tostate.items()}
        #self.goal = 62
        self.goal = self.tostate[(5, 21)]
        self.init_states = list(range(self.observation_space.n))
        self.init_states.remove(self.goal)
        self.viewer = None
        self.currentcell_obj = None

    def empty_around(self, cell):
        avail = []
        for action in range(self.action_space.n):
            nextcell = tuple(cell + self.directions[action])
            if not self.occupancy[nextcell]:
                avail.append(nextcell)
        return avail

    def to_cell(self, index):
        return self.tocell[index]

    def reset(self):
        state = self.rng.choice(self.init_states)
        self.currentcell = self.tocell[state]
        return state

    def step(self, action):
        """
        The agent can perform one of four actions,
        up, down, left or right, which have a stochastic effect. With probability 2/3, the actions
        cause the agent to move one cell in the corresponding direction, and with probability 1/3,
        the agent moves instead in one of the other three directions, each with 1/9 probability. In
        either case, if the movement would take the agent into a wall then the agent remains in the
        same cell.

        We consider a case in which rewards are zero on all state transitions.
        """
        nextcell = tuple(self.currentcell + self.directions[action])
        if not self.occupancy[nextcell]:
            self.currentcell = nextcell
            if self.rng.uniform() < 1/3.:
                empty_cells = self.empty_around(self.currentcell)
                self.currentcell = empty_cells[self.rng.randint(len(empty_cells))]

        state = self.tostate[self.currentcell]
        done = state == self.goal
        return state, float(done), done, None

    def draw_square(self, start_x, start_y, length_x, length_y, color):
        color_dict = {
            'white':[1,1,1],
            'black':[0,0,0],
            'red':[1,0,0],
            'blue':[0,0,1],
            'green':[0,1,0]
        }
        cell = rendering.make_polygon([(start_x, start_y), (start_x+length_x, start_y), (start_x + length_x, start_y + length_y), (start_x, start_y+length_y)])
        if color_dict.get(color) != None:
            cell.set_color(color_dict[color][0], color_dict[color][1], color_dict[color][2])
            self.viewer.add_geom(cell)
        return cell

    def render(self, mode='Human', close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return
        
        length_x = 30
        length_y = 30
        screen_height =  length_x * self.occupancy.shape[0]
        screen_width = length_y * self.occupancy.shape[1]
        position_x = 0
        position_y = 0

        current_position_x = self.currentcell[1] * length_x 
        current_position_y = self.currentcell[0] * length_y

        if self.viewer is None:
            goal_state = self.to_cell(self.goal)
            self.viewer = rendering.Viewer(screen_width, screen_height)
            for i in range(self.occupancy.shape[0]):
                for j in range(self.occupancy.shape[1]):
                    if self.occupancy[i][j] == 1:
                        color = 'black'
                    elif goal_state[0] == i and goal_state[1] == j:
                        color = 'red'
                    elif self.currentcell[0] == i and self.currentcell[1] == j:
                        color = 'blue'
                        self.currentcell_obj = self.draw_square(position_x, position_y, length_x, length_y, color)
                    else:
                        position_x += length_x
                        continue
                    self.draw_square(position_x, position_y, length_x, length_y, color)
                    position_x += length_x
                position_x = 0
                position_y += length_y
        else:
            self.currentcell_obj.v = [(current_position_x, current_position_y), (current_position_x+length_x, current_position_y), (current_position_x + length_x, current_position_y + length_y), (current_position_x, current_position_y+length_y)]
        return self.viewer.render(return_rgb_array = mode=='rgb_array')