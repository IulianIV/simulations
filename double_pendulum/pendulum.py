import pygame
import math

PI = math.pi


class Pendulum:

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
    def angle(self):
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

    def draw(self, surface: pygame.display, origin: list,  end: list):

        pygame.draw.line(surface, self.rod_color, origin, end, 2)
        pygame.draw.circle(surface, self.ball_color, end, self.ball_mass)

    def draw_rod(self, surface: pygame.display, origin: list, end: list):
        pygame.draw.line(surface, self.rod_color, origin, end, 2)

    def draw_ball(self, surface: pygame.display,  end: list):
        pygame.draw.circle(surface, self.ball_color, end, self.ball_mass)


class DoublePendulum(Pendulum):

    def __init__(self, rod_color: tuple, ball_color: tuple, length: float = 100, rod_mass: float = 10,
                 ball_mass: float = 10, angle: float = PI):
        super().__init__(rod_color, ball_color, length, length, rod_mass, ball_mass, angle)

