import numpy as np

import pyglet
import gym
from gym import core, spaces
from gym.envs.registration import register
from gym.envs.classic_control import rendering
from gym_fourrooms.envs.fourrooms import Fourrooms


class Fiverooms(Fourrooms):
    def __init__(self):
        super(Fiverooms, self).__init__()
        
    def get_layout(self):
        layout = """\
wwwwwwwwwwwwwwwwwwww
w     w            w
w     w     w      w
w           w      w
w     w     w      w
w     w     w      w
ww wwww     w      w
w     www www      w
w     w     w      w
w     w     w      w
w           w      w
w     w     w      w
wwwwwwwwwwwwwwwwwwww
"""
        return layout
