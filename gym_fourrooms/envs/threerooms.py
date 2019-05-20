import numpy as np

import pyglet
import gym
from gym import core, spaces
from gym.envs.registration import register
from gym.envs.classic_control import rendering
from gym_fourrooms.envs.fourrooms import Fourrooms


class Threerooms(Fourrooms):
    def __init__(self):
        super(Threerooms, self).__init__()
        
    def get_layout(self):
        layout = """\
wwwwwwwwwwwwwwwwwwwwwww
w     w     w         w
w     w     w         w
w                     w
w     w     w         w
w     w     w         w
wwwwwwwwwwwwwwwwwwwwwww
"""
        return layout
