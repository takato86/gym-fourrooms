from abc import ABCMeta, abstractmethod


class ShapingRewardBase(metaclass=ABCMeta):
    __slots__ = ("value")
    @abstractmethod
    def perform(self, curr_state, next_state):
        pass


class DefaultReward(ShapingRewardBase):
    def __init__(self, value):
        self.value = 0

    def perform(self, curr_state, next_state):
        return self.value
