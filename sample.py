import gym
import gym_fourrooms

env = gym.make('Fourrooms-v0')
env.reset()
env.render()
env.step(0)
env.render()