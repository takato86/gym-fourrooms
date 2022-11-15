from gym_fourrooms.envs.fourrooms import Rooms, ConstRooms


class Tworooms(Rooms):
    def __init__(self):
        super(Tworooms, self).__init__()
        self.goal = self.tostate[(1, 14)]
        self.init_states.remove(self.goal)

    def get_layout(self):
        layout = """\
wwwwwwwwwwwwwwwwww
w      w         w
w      w         w
w                w
w      w         w
w      w         w
wwwwwwwwwwwwwwwwww
"""
        return layout


class PenalizedTworooms(ConstRooms):
    def __init__(self):
        super().__init__()
        self.goal = 14
        self.init_states = [0]
        self.penalized_states = [25, 42, 57]
        self.subgoals = {}
    
    def reset(self, subgoals={}):
        self.subgoals = {}
        if self.viewer is not None:
            self.viewer = None
        self.__set_subgoals(subgoals)
        return super().reset()

    def __set_subgoals(self, subgoals):
        for k, v in subgoals.items():
            if isinstance(k, int):
                self.subgoals[k] = v
            else:
                self.subgoals[self.tostate[k]] = v

    
    def get_layout(self):
        layout = """\
wwwwwwwwwwwwwwwwwww
w     w     w     w
w     w     w     w
w                 w
w     w     w     w
w     w     w     w
w     w     w     w
wwwwwwwwwwwwwwwwwww
"""
        return layout

    def step(self, action):
        state, reward, done, info = super().step(action)
        if state in self.penalized_states:
            reward = -0.002
        return state, reward, done, info

    def render(self, mode='Human', close=False):
        super().render(mode, close)
        length_x = 30
        length_y = 30
        screen_height = length_x * self.occupancy.shape[0]
        # screen_width = length_y * self.occupancy.shape[1]
        position_x = 0
        position_y = screen_height - length_y

        for state, _ in self.subgoals.items():
            y, x = self.to_cell(state)
            position_x = x * length_x
            position_y = screen_height - (y + 1) * length_y
            self.draw_square(position_x, position_y, length_x, length_y, "green")
        
        return self.viewer.render(return_rgb_array=mode == 'rgb_array')
    
    
class PenalizedTworoomsThrough(PenalizedTworooms):
    def __init__(self):
        super().__init__()
        self.penalized_states = [25, 57]
