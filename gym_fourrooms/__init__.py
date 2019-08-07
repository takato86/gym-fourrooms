import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Oneroom-v0',
    entry_point='gym_fourrooms.envs:Oneroom',
    timestep_limit=20000,
    reward_threshold=1,
)

register(
    id = 'SubGoalFourrooms-v0',
    entry_point = 'gym_fourrooms.envs:SubGoalFourrooms',
    timestep_limit = 20000,
    reward_threshold = 1
)

register(
    id='ConstOneroom-v0',
    entry_point='gym_fourrooms.envs:ConstOneroom',
    timestep_limit=20000,
    reward_threshold=1,
)

register(
    id='GoalsOneroom-v0',
    entry_point='gym_fourrooms.envs:GoalsOneroom',
    timestep_limit=20000,
    reward_threshold=1,
)

register(
    id='Tworooms-v0',
    entry_point='gym_fourrooms.envs:Tworooms',
    timestep_limit=20000,
    reward_threshold=1,
)

register(
    id='Fourrooms-v0',
    entry_point='gym_fourrooms.envs:Fourrooms',
    timestep_limit=20000,
    reward_threshold=1,
)

register(
    id='Fourrooms-v1',
    entry_point='gym_fourrooms.envs:FourroomsV1',
    timestep_limit=20000,
    reward_threshold=1,
)

register(
    id='ConstFourrooms-v0',
    entry_point='gym_fourrooms.envs:ConstFourrooms',
    timestep_limit=20000,
    reward_threshold=1,
)

register(
    id='ShapingFourrooms-v0',
    entry_point='gym_fourrooms.envs:ShapingFourrooms',
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

