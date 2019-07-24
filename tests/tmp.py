import gym
import gym_fourrooms

env = gym.make("SubGoalFourrooms-v0")
env.reset()
subgoals = {(4,7) : 0.5, 59 : 0.5}
test_subgoals = {35 : 0.5, 59 : 0.5}
env.env.set_subgoals(subgoals)
