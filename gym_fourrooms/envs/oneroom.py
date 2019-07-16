import numpy as np

import pyglet
import gym
from gym import core, spaces
from gym.envs.registration import register
from gym.envs.classic_control import rendering
from gym_fourrooms.envs.rooms import Rooms, ConstRooms, GoalsRooms


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

class ConstOneroom(ConstRooms):
    def __init__(self):
        super(ConstOneroom, self).__init__()
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

class GoalsOneroom(GoalsRooms):
    def __init__(self):
        super(GoalsOneroom, self).__init__()
        goals = [(5, 10), (1, 10)]
        self.goals = [self.tostate[goal] for goal in goals]
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