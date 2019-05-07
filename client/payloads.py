from enum import Enum, unique


@unique
class ControlPayload(Enum):
    FORWARD = 'FORWARD',
    BACKWARD = 'BACKWARD',
    LEFT = 'LEFT',
    RIGHT = 'RIGHT',
    STOP = 'STOP',
    STRAIGHT = 'STRAIGHT'


@unique
class SpeedPayload(Enum):
    SLOW = 'SLOW',
    MEDIUM = 'MEDIUM',
    FAST = 'FAST'
