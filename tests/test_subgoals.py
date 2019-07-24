import gym
import gym_fourrooms
import unittest
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestSubGoalRooms(unittest.TestCase):
    def define_mock(self):
        pass
    
    def test_step(self):
        env = gym.make("SubGoalFourrooms-v0")
        env.reset()
        subgoals = {59 : 0.5}
        test_subgoals = {59 : 0.5}
        # subgoals = {(4,7) : 0.5, 59 : 0.5}
        # test_subgoals = {36 : 0.5, 59 : 0.5}
        env.env.set_subgoals(subgoals)
        done = False
        while(1):
            act = np.random.choice([0,1,2,3])
            obs, rwd, done, _ = env.step(act)
            if obs in test_subgoals.keys():
                logger.info(obs)
                self.assertEquals(0.5, rwd)
                return
            if done:
                logger.info("Reset env")
                env.reset()
