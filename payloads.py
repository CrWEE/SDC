from enum import Enum, unique


@unique
class ControlPayload(Enum):
    FORWARD = 1,
    BACKWARD = 2,
    LEFT = 3,
    RIGHT = 4,
    STOP = 5,
    STRAIGHT = 6


@unique
class SpeedPayload(Enum):
    SLOW = 1,
    MEDIUM = 2,
    FAST = 3
