from __future__ import annotations
from abc import ABC, abstractmethod
import pygame
import math

PI = math.pi


class Pendulum(ABC):

    @abstractmethod
    def __init__(self, rod_color: tuple, ball_color: tuple, length: float = 100, rod_mass: float = 10,
                 ball_mass: float = 10, angle: float = PI):
        self.length = length
        self.rod_mass = rod_mass
        self.ball_mass = ball_mass
        self.mass = self.rod_mass + self.ball_mass
        self._angle = angle
        self.rod_color = rod_color
        self.ball_color = ball_color
        self._x = 0
        self._y = 0
        self._coords = self.get_coords
        self._velocity = 0
        self._acceleration = 0

    @property
    @abstractmethod
    def x(self) -> float:
        pass

    @property
    @abstractmethod
    def y(self) -> float:
        pass

    @abstractmethod
    def update_y(self):
        pass

    @property
    @abstractmethod
    def get_coords(self) -> list:
        pass

    @property
    @abstractmethod
    def angle(self) -> float:
        pass

    @property
    @abstractmethod
    def acceleration(self) -> float:
        pass

    @property
    @abstractmethod
    def velocity(self) -> float:
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
    def p1_motion_model(self, ga: float, second_pendulum: Pendulum):
        pass

    @abstractmethod
    def p2_motion_model(self, ga:float, first_pendulum: Pendulum):
        pass


class DoublePendulum(Pendulum):
    def __init__(self, rod_color: tuple, ball_color: tuple, length: float = 100, rod_mass: float = 10,
                 ball_mass: float = 10, angle: float = PI):
        self.length = length
        self.rod_mass = rod_mass
        self.ball_mass = ball_mass
        self.mass = self.rod_mass + self.ball_mass
        self._angle = angle
        self.rod_color = rod_color
        self.ball_color = ball_color
        self._x = 0
        self._y = 0
        self._coords = self.get_coords
        self._velocity = 0
        self._acceleration = 0

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, new_x: float):
        self._x = new_x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, new_y: float):
        self._y = new_y

    @property
    def get_coords(self):
        coords = [self._y, self._y]

        return coords

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, new_angle: float):
        self._angle = new_angle

    @property
    def acceleration(self):
        return self._acceleration

    @acceleration.setter
    def acceleration(self, new_acceleration: float):
        self._acceleration = new_acceleration

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, vel: float):
        self._velocity = vel

    def draw_rod(self, surface: pygame.display, origin: list, end: list):
        pygame.draw.line(surface, self.rod_color, origin, end, 2)

    def draw_ball(self, surface: pygame.display, end: list):
        pygame.draw.circle(surface, self.ball_color, end, self.ball_mass)

    def draw(self, surface: pygame.display, origin: list, end: list):
        self.draw_rod(surface, origin, end)
        self.draw_ball(surface, end)

    def p1_motion_model(self, ga: float, second_pendulum: Pendulum):
        """

        :param ga: gravitational acceleration
        :param second_pendulum: secondary pendulum
        :return: motion model of first pendulum
        """
        equation_1: float = - ga * ((2 * self.mass) + second_pendulum.mass) * math.sin(self.angle)
        equation_2: float = second_pendulum.mass * ga * math.sin(self.angle - (2 * second_pendulum.angle))
        equation_3: float = 2 * math.sin(self.angle - second_pendulum.angle) * second_pendulum.mass
        equation_4: float = (
                (second_pendulum.velocity ** 2 * second_pendulum.length) +
                (self.velocity ** 2 * self.length * math.cos(self.angle - second_pendulum.angle)))
        denominator_1: float = self.length * (
                (2 * self.mass) + second_pendulum.mass -
                second_pendulum.mass * math.cos((2 * self.angle) - (2 * second_pendulum.angle)))

        self.acceleration = (equation_1 - equation_2 - equation_3 * equation_4) / denominator_1

        return self.acceleration

    def p2_motion_model(self, ga: float, first_pendulum: Pendulum):
        """
        :param ga: gravitational acceleration
        :param first_pendulum: first pendulum
        :return: motion model of second pendulum
        """
        equation_1: float = 2 * math.sin(first_pendulum.angle - self.angle)
        equation_2: float = (first_pendulum.velocity ** 2 * first_pendulum.length * (first_pendulum.mass + self.mass))
        equation_3: float = ga * (first_pendulum.mass + self.mass) * math.cos(first_pendulum.angle)
        equation_4: float = self.velocity ** 2 * self.length * self.mass * math.cos(first_pendulum.angle - self.angle)
        denominator_2: float = self.length * (2 * first_pendulum.mass + self.mass - self.mass *
                                              math.cos(2 * first_pendulum.angle - 2 * self.angle))

        self.acceleration = (equation_1 * (equation_2 + equation_3 + equation_4)) / denominator_2

        return self.acceleration
