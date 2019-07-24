import numpy as np

import pyglet
import gym
from gym import core, spaces
from gym.envs.registration import register
from gym.envs.classic_control import rendering
from gym_fourrooms.envs.rooms import Rooms, ConstRooms

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

class ConstFourrooms(ConstRooms):
    def __init__(self):
        super(ConstFourrooms, self).__init__()
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

class SubGoalFourrooms(Fourrooms):
    def __init__(self):
        """Fourrooms env with rewards as sugoals
        
        Arguments:
            Fourrooms {[type]} -- [description]
            subgoals {[type]} -- {(x, y): value}
        """
        super(SubGoalFourrooms, self).__init__()
        self.subgoals = {}

    def set_subgoals(self, subgoals):
        for k, v in subgoals.items():
            if isinstance(k, int):
                self.subgoals[k] = v
            else:
                self.subgoals[self.tostate[k]] = v

    def step(self, act):
        next_state, reward, done, info = super(SubGoalFourrooms, self).step(act)
        if self.subgoals.get(next_state) is not None:
            reward += self.subgoals[next_state]
        return next_state, reward, done, info

