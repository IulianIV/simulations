from __future__ import annotations
from abc import ABC, abstractmethod
import pygame

from utils import MathematicalConstants


class BasicPendulum(ABC):

    @abstractmethod
    def __init__(self, rod_color: tuple, ball_color: tuple, length: float = 100, rod_mass: float = 10,
                 ball_mass: float = 10, angle: float = MathematicalConstants.PI):
        self.length = length
        self.rod_mass = rod_mass
        self.ball_mass = ball_mass
        self.mass = self.rod_mass + self.ball_mass
        self._angle = angle
        self.rod_color = rod_color
        self.ball_color = ball_color

    @property
    @abstractmethod
    def x(self) -> float:
        pass

    @x.setter
    @abstractmethod
    def x(self, new_x):
        pass

    @abstractmethod
    def calculate_new_x(self) -> float:
        pass

    @property
    @abstractmethod
    def y(self) -> float:
        pass

    @y.setter
    @abstractmethod
    def y(self, new_y):
        pass

    @abstractmethod
    def calculate_new_y(self) -> float:
        pass

    @property
    @abstractmethod
    def get_coords(self) -> list:
        pass

    @property
    @abstractmethod
    def angle(self) -> float:
        pass

    @angle.setter
    @abstractmethod
    def angle(self, new_angle):
        pass

    @abstractmethod
    def update_angle(self) -> float:
        pass

    @property
    @abstractmethod
    def acceleration(self) -> float:
        pass

    @acceleration.setter
    @abstractmethod
    def acceleration(self, new_acc):
        pass

    @property
    @abstractmethod
    def velocity(self) -> float:
        pass

    @velocity.setter
    @abstractmethod
    def velocity(self, new_vel):
        pass

    @abstractmethod
    def update_velocity(self) -> float:
        pass

    @abstractmethod
    def draw_rod(self, surface: pygame.display, origin: list, end: list):
        pass

    @abstractmethod
    def draw_ball(self, surface: pygame.display, end: list):
        pass

    @abstractmethod
    def draw(self, surface: pygame.display, origin: list, end: list):
        pass

    @abstractmethod
    def get_data(self, pendulum_property):
        pass

