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
