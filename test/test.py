import gym
import gym_fourrooms

env = gym.make("ConstFourrooms-v0")
env = gym.make("ConstOneroom-v0")
env = gym.make("GoalsOneroom-v0")

env.reset()
for i in range(1000):
    env.render()
