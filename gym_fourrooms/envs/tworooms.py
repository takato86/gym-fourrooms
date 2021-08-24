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
        if state in [25, 42, 57]:
            reward = -0.002
        return state, reward, done, info
