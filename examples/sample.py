import gym
import gym_fourrooms


def main():
    env = gym.make("FlexibleFourrooms-v0")    
    env.env.set_init_states([(i, j) for i in range(1,6) for j in range(1,6)])
    env.reset() 
    env.env.set_goal((3,6))
    [env.render() for i in range(1000)]

if __name__ == "__main__":
    main()