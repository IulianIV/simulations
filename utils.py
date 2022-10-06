from dataclasses import dataclass
import math


@dataclass
class Colors:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)


@dataclass
class Screen:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000
    SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
    CENTER_WIDTH = SCREEN_WIDTH / 2
    CENTER_HEIGHT = SCREEN_HEIGHT / 2
    Y_OFFSET = 200


@dataclass
class Fonts:
    STANDARD_FONT = 'Times New Roman'


@dataclass
class MathematicalConstants:
    GRAVITY = 1
    PI = math.pi