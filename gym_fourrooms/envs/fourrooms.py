from gym_fourrooms.envs.rooms import Rooms, ConstRooms,\
                                     ShapingRooms, FlexibleRooms


class Fourrooms(Rooms):
    def __init__(self):
        super(Fourrooms, self).__init__()
        self.goal = 62
        # self.goal = self.tostate[(5, 21)]
        self.init_states.remove(self.goal)

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


class FourroomsV1(Fourrooms):
    def __init__(self):
        super(FourroomsV1, self).__init__()

    def step(self, act):
        next_state, reward, done, info = super(FourroomsV1, self).step(act)
        if not done:
            reward -= 1
        return next_state, reward, done, info


class FlexibleFourrooms(FlexibleRooms):
    def __init__(self):
        super(FlexibleFourrooms, self).__init__()
        self.goal = 62

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


class ConstFourrooms(ConstRooms):
    def __init__(self):
        super(ConstFourrooms, self).__init__()
        self.goal = self.tostate[(11, 11)]
        # self.goal = self.tostate[(5, 21)]
        # self.init_states.remove(self.goal)
        self.init_states = [0]

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


class ConstStepFourrooms(ConstFourrooms):
    def __init__(self):
        super().__init__()

    def step(self, act):
        next_state, reward, done, info = super().step(act)
        if not done:
            reward = -1
        else:
            reward = 0
        return next_state, reward, done, info


class DiagonalFourrooms(ConstFourrooms):
    def __init__(self):
        super().__init__()

    def get_layout(self):
        layout = """\
wwwwwwwwwwwww
w      w   ww
w         w w
w    w   w  w
w   w   w   w
w  w   w    w
w w   w   w w
ww   w   w  w
w   w   w   w
w      w    w
w w   w     w
ww   w      w
wwwwwwwwwwwww
"""
        return layout


class DiagonalPartialFourrooms(ConstFourrooms):
    def __init__(self):
        super().__init__()

    def get_layout(self):
        layout = """\
wwwwwwwwwwwww
w      w    w
w           w
w    w      w
w   w       w
w  w w     ww
w     w   w w
ww     w    w
w       w   w
w      w    w
w           w
w    w      w
wwwwwwwwwwwww
"""
        return layout


# TODO v0とv1のどちらかをベースに
class SubGoalFourrooms(Fourrooms):
    def __init__(self):
        """Fourrooms env with rewards as sugoals

        Arguments:
            Fourrooms {[type]} -- [description]
            subgoals {[type]} -- {(x, y): value}
        """
        super(SubGoalFourrooms, self).__init__()
        self.init_states = [0]
        self.goal = self.tostate[(11, 11)]
        self.subgoals = {}

    def reset(self, subgoals):
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

    def step(self, act):
        next_state, reward, done, info \
            = super(SubGoalFourrooms, self).step(act)
        if self.subgoals.get(next_state) is not None:
            reward += self.subgoals[next_state]
        reward -= 1
        return next_state, reward, done, info

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

class LargeFourrooms(SubGoalFourrooms):
    def __init__(self):
        super(LargeFourrooms, self).__init__()
        self.goal = self.tostate[(16, 31)]

    def get_layout(self):
        layout = """\
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
w             w                 w
w             w                 w
w                               w
w             w                 w
w             w                 w
w             w                 w
w             w                 w
wwwww wwwwwwwww                 w
w             wwwwwww wwwwwwwwwww
w             w                 w
w             w                 w
w                               w
w             w                 w
w             w                 w
w             w                 w
w             w                 w
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
"""
        return layout


class ConstLargeFourrooms(ConstRooms):
    def __init__(self):
        super().__init__()
        self.goal = 453

    def get_layout(self):
        layout = """\
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
w             w                 w
w             w                 w
w                               w
w             w                 w
w             w                 w
w             w                 w
w             w                 w
wwwww wwwwwwwww                 w
w             wwwwwww wwwwwwwwwww
w             w                 w
w             w                 w
w                               w
w             w                 w
w             w                 w
w             w                 w
w             w                 w
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
"""
        return layout


class ShapingFourrooms(ShapingRooms):
    def __init__(self):
        super(ShapingFourrooms, self).__init__()
        self.goal = 62
        # self.goal = self.tostate[(5, 21)]
        self.init_states.remove(self.goal)

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
