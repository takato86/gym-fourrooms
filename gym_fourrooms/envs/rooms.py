import numpy as np

import pyglet
import gym
from gym import core, spaces
from gym.envs.registration import register
from gym.envs.classic_control import rendering
from matplotlib import cm
from gym_fourrooms.envs.shaping_reward import ShapingRewardBase,\
                                              DefaultReward

class Rooms(gym.Env):
    metadata = {'render.modes': ['human', 'rgb_array']}
    def __init__(self):

        layout = self.get_layout()
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
        self.init_states = list(range(self.observation_space.n))
        self.viewer = None
        self.currentcell_obj = None
        self.n_steps = 0
        self.curr_option = None
        self.goal = None
    
    def set_option(self, option):
        self.curr_option = option

    def get_layout(self):
        layout = """\
wwwwwwwwwwwww
w     w     w
w     w     w
w           w
w     w     w
w     w     w
ww wwww     w
w     www www
w     w     w
w     w     w
w           w
w     w     w
wwwwwwwwwwwww
"""
        return layout

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
        self.n_steps = 0
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
            if self.rng.uniform() < 1/3.:
                empty_cells = self.empty_around(self.currentcell)
                self.currentcell = empty_cells[self.rng.randint(len(empty_cells))]
            else:
                self.currentcell = nextcell
        self.n_steps += 1
        state = self.tostate[self.currentcell]
        done = False
        reward = 0.0
        if state == self.goal:
            done = True
            reward = 1.0
        if self.n_steps >= 1000:
            done = True
            reward = 0.0
        return state, reward, done, None

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
        elif type(color) == int:
            cmap = cm.Paired(color)
            cell.set_color(cmap[0], cmap[1], cmap[2])
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
        position_y = screen_height - length_y

        current_position_x = self.currentcell[1] * length_x 
        current_position_y = self.currentcell[0] * length_y

        goal_state = self.to_cell(self.goal)
        if self.viewer is None:
            self.viewer = rendering.Viewer(screen_width, screen_height)
        self.viewer.geoms = []
        for i in range(self.occupancy.shape[0]):
            for j in range(self.occupancy.shape[1]):
                if self.occupancy[i][j] == 1:
                    color = 'black'
                elif goal_state[0] == i and goal_state[1] == j:
                    color = 'red'
                elif self.currentcell[0] == i and self.currentcell[1] == j:
                    if self.curr_option != None:
                        color = self.curr_option
                    else:
                        color = 'blue'
                    self.currentcell_obj = self.draw_square(position_x, position_y, length_x, length_y, color)
                else:
                    position_x += length_x
                    continue
                self.draw_square(position_x, position_y, length_x, length_y, color)
                position_x += length_x
            position_x = 0
            position_y -= length_y
        return self.viewer.render(return_rgb_array = mode=='rgb_array')

class FlexibleRooms(Rooms):
    def __init__(self):
        super(FlexibleRooms, self).__init__()
    
    def set_init_states(self, init_states):
        """スタート状態の指定
        
        Arguments:
            init_states {[list<tuple>]} -- スタート状態をタプルリストで指定する．
        """
        self.init_states = [self.tostate[init_state] for init_state in init_states ]

    def set_goal(self, goal:tuple):
        self.goal = self.tostate[goal]


class ShapingRooms(Rooms):
    def __init__(self):
        super(ShapingRooms, self).__init__()
        self.shaping_reward = DefaultReward(value=0)
        
    def set_shaping_reward(self, shaping_reward):
        self.shaping_reward = shaping_reward
    
    def step(self, action):
        prev_state = self.tostate[self.currentcell]
        nextcell = tuple(self.currentcell + self.directions[action])
        if not self.occupancy[nextcell]:
            if self.rng.uniform() < 1/3.:
                empty_cells = self.empty_around(self.currentcell)
                self.currentcell = empty_cells[self.rng.randint(len(empty_cells))]
            else:
                self.currentcell = nextcell
        self.n_steps += 1
        state = self.tostate[self.currentcell]
        done = False
        reward = self.shaping_reward.perform(prev_state, state)
        if state == self.goal:
            done = True
            reward = 1.0
        if self.n_steps >= 1000:
            done = True
            reward = 0.0
        return state, reward, done, None


class ConstRooms(Rooms):
    def __init__(self):
        super(ConstRooms, self).__init__()
    
    def step(self, action):
        nextcell = tuple(self.currentcell + self.directions[action])
        if not self.occupancy[nextcell]:
            self.currentcell = nextcell
        self.n_steps += 1
        state = self.tostate[self.currentcell]
        done = False
        reward = 0.0
        if state == self.goal:
            done = True
            reward = 1.0
        if self.n_steps >= 1000:
            done = True
            reward = 0.0
        return state, reward, done, None

class GoalsRooms(Rooms):
    def __init__(self):
        super(GoalsRooms, self).__init__()
    
    def step(self, action):
        nextcell = tuple(self.currentcell + self.directions[action])
        if not self.occupancy[nextcell]:
            if self.rng.uniform() < 1/3.:
                empty_cells = self.empty_around(self.currentcell)
                self.currentcell = empty_cells[self.rng.randint(len(empty_cells))]
            else:
                self.currentcell = nextcell
        self.n_steps += 1
        state = self.tostate[self.currentcell]
        done = False
        reward = 0.0
        if state == self.goal:
            done = True
            reward = 1.0
        if self.n_steps >= 1000:
            done = True
            reward = 0.0
        if done:
            self.n_steps = 0
        return state, float(done), done, None
    
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
        position_y = screen_height - length_y

        current_position_x = self.currentcell[1] * length_x 
        current_position_y = self.currentcell[0] * length_y

        goal_states = [self.to_cell(goal) for goal in self.goals]
        if self.viewer is None:
            self.viewer = rendering.Viewer(screen_width, screen_height)
        self.viewer.geoms = []
        for i in range(self.occupancy.shape[0]):
            for j in range(self.occupancy.shape[1]):
                if self.occupancy[i][j] == 1:
                    color = 'black'
                elif (i,j) in goal_states:
                    color = 'red'
                elif self.currentcell[0] == i and self.currentcell[1] == j:
                    if self.curr_option != None:
                        color = self.curr_option
                    else:
                        color = 'blue'
                    self.currentcell_obj = self.draw_square(position_x, position_y, length_x, length_y, color)
                else:
                    position_x += length_x
                    continue
                
                self.draw_square(position_x, position_y, length_x, length_y, color)
                position_x += length_x
            position_x = 0
            position_y -= length_y
        return self.viewer.render(return_rgb_array = mode=='rgb_array')
