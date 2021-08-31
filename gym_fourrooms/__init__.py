import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Oneroom-v0',
    entry_point='gym_fourrooms.envs:Oneroom',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='SubGoalFourrooms-v0',
    entry_point='gym_fourrooms.envs:SubGoalFourrooms',
    max_episode_steps=20000,
    reward_threshold=1
)

register(
    id='ConstOneroom-v0',
    entry_point='gym_fourrooms.envs:ConstOneroom',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='GoalsOneroom-v0',
    entry_point='gym_fourrooms.envs:GoalsOneroom',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='Tworooms-v0',
    entry_point='gym_fourrooms.envs:Tworooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='PenalizedTworooms-v0',
    entry_point='gym_fourrooms.envs:PenalizedTworooms',
    max_episode_steps=20000,
    reward_threshold=1,
)


register(
    id='PenalizedTworoomsThrough-v0',
    entry_point='gym_fourrooms.envs:PenalizedTworoomsThrough',
    max_episode_steps=20000,
    reward_threshold=1,
)


register(
    id='Fourrooms-v0',
    entry_point='gym_fourrooms.envs:Fourrooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='Fourrooms-v1',
    entry_point='gym_fourrooms.envs:FourroomsV1',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='FlexibleFourrooms-v0',
    entry_point='gym_fourrooms.envs:FlexibleFourrooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='DiagonalFourrooms-v0',
    entry_point='gym_fourrooms.envs:DiagonalFourrooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='DiagonalPartialFourrooms-v0',
    entry_point='gym_fourrooms.envs:DiagonalPartialFourrooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='LargeFourrooms-v1',
    entry_point='gym_fourrooms.envs:LargeFourrooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='ConstFourrooms-v0',
    entry_point='gym_fourrooms.envs:ConstFourrooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='ConstLargeFourrooms-v0',
    entry_point='gym_fourrooms.envs:ConstLargeFourrooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='ShapingFourrooms-v0',
    entry_point='gym_fourrooms.envs:ShapingFourrooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='Threerooms-v0',
    entry_point='gym_fourrooms.envs:Threerooms',
    max_episode_steps=20000,
    reward_threshold=1,
)

register(
    id='Fiverooms-v0',
    entry_point='gym_fourrooms.envs:Fiverooms',
    max_episode_steps=20000,
    reward_threshold=1,
)
