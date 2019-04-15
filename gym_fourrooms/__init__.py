from gym.envs.registration import register

register(
    id='Fourrooms-v0',
    entry_point='gym_fourrooms.envs:Fourrooms',
    timestep_limit=20000,
    reward_threshold=1,
)
