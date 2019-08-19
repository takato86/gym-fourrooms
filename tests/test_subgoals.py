import gym
import gym_fourrooms
import unittest
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestLargeSubGoalRooms(unittest.TestCase):
    def define_mock(self):
        pass
    
    def test_step(self):
        env = gym.make("LargeFourrooms-v1")
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
                self.assertEqual(0.5 - 1, rwd)
                return
            if done:
                logger.info("Reset env")
                env.reset()


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
                self.assertEqual(0.5 - 1, rwd)
                return
            if done:
                logger.info("Reset env")
                env.reset()

class TestRoomsV1(unittest.TestCase):
    def define_mock(self):
        pass
    
    def test_step(self):
        env = gym.make("Fourrooms-v1")
        env.reset()
        done = False
        is_flag =[False, False]
        while(1):
            act = np.random.choice([0,1,2,3])
            obs, rwd, done, _ = env.step(act)
            if obs == 62:
                is_flag[0] = True
                self.assertEqual(1, rwd)
            else:
                is_flag[1] = True
                logger.info(obs)
                self.assertEqual(-1, rwd)
            if done:
                logger.info("Reset env")
                if all(is_flag):
                    return
                env.reset()