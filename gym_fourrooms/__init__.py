import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Fourrooms-v0',
    entry_point='gym_fourrooms.envs:Fourrooms',
    timestep_limit=20000,
    reward_threshold=1,
)

register(
    id='Threerooms-v0',
    entry_point='gym_fourrooms.envs:Threerooms',
    timestep_limit=20000,
    reward_threshold=1,
)

register(
    id='Fiverooms-v0',
    entry_point='gym_fourrooms.envs:Fiverooms',
    timestep_limit=20000,
    reward_threshold=1,
)
