import numpy as np

import pyglet
import gym
from gym import core, spaces
from gym.envs.registration import register
from gym.envs.classic_control import rendering
from gym_fourrooms.envs.fourrooms import Rooms


class Oneroom(Rooms):
    def __init__(self):
        super(Oneroom, self).__init__()
        self.goal = self.tostate[(5, 10)]
        self.init_states.remove(self.goal)
        
    def get_layout(self):
        layout = """\
wwwwwwwwwwwww
w           w
w           w
w           w
w           w
w           w
wwwwwwwwwwwww
"""
        return layout
