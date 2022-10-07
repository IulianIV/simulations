import pygame
import math
from engine.bodies.pendulum import BasicPendulum
from utils import MathematicalConstants

# TODO maybe the motion simulation should be in the DoublePendulumSimulation and this class renamed and inherit from
#   Pendulum. This naming would be more consistent and passing 2 pendulums (not doubles) to simulation makes more sense


class Pendulum(BasicPendulum):
    def __init__(self, rod_color: tuple, ball_color: tuple, length: float = 100, rod_mass: float = 10,
                 ball_mass: float = 10, angle: float = MathematicalConstants.PI):
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

    def calculate_new_x(self, offset: int = None, pendulum: BasicPendulum = None):
        if pendulum is not None:
            self.x = pendulum.x + self.length * math.sin(self.angle)
        else:
            self.x = self.length * math.sin(self.angle) + offset

        return self.x

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, new_y: float):
        self._y = new_y

    def calculate_new_y(self, offset: int = None, pendulum: BasicPendulum = None) -> float:
        if pendulum is not None:
            self.y = pendulum.y + self.length * math.cos(self.angle)
        else:
            self.y = self.length * math.cos(self.angle) + offset

        return self.y

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

    def update_angle(self) -> float:
        self.angle += self.velocity

        return self.angle

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

    def update_velocity(self) -> float:
        self.velocity += self.acceleration

        return self.velocity

    def draw_rod(self, surface: pygame.display, origin: list, end: list):
        pygame.draw.line(surface, self.rod_color, origin, end, 2)

    def draw_ball(self, surface: pygame.display, end: list):
        pygame.draw.circle(surface, self.ball_color, end, self.ball_mass)

    def draw(self, surface: pygame.display, origin: list, end: list):
        self.draw_rod(surface, origin, end)
        self.draw_ball(surface, end)

    # TODO Improve this method to be more user friendly
    def get_data(self, pendulum_property):
        self_attributes = dir(self)

        if pendulum_property not in self_attributes:
            return f'Attribute {pendulum_property} is not a member of {self.__class__.__name__}'

        data = ''.join('Pendulum {property} value is: {property_value:.2f}'
                       .format(property=pendulum_property, property_value=getattr(self, pendulum_property)))

        return data


class DoublePendulum:
    def __init__(self, pendulum_1: Pendulum, pendulum_2: Pendulum,
                 gravity: float, origin=None):
        if origin is None:
            origin = [0, 0]
        self.p1 = pendulum_1
        self.p2 = pendulum_2
        self.ga = gravity
        self.origin = origin

    def __p1_x_y(self):
        self.p1.calculate_new_x(self.origin[0])
        self.p1.calculate_new_y(self.origin[1])

    def __p2_x_y(self):
        self.p2.calculate_new_x(pendulum=self.p1)
        self.p2.calculate_new_y(pendulum=self.p1)

    def calculate_new_x_y(self):
        self.__p1_x_y()
        self.__p2_x_y()

    def __update_velocity(self):
        self.p1.update_velocity()
        self.p2.update_velocity()

    def update_velocity(self):
        self.__update_velocity()

    def ___update_angle(self):
        self.p1.update_angle()
        self.p2.update_angle()

    def update_angle(self):
        self.___update_angle()

    def __p1_motion_model(self):
        equation_1: float = - self.ga * ((2 * self.p1.mass) + self.p2.mass) * math.sin(self.p1.angle)
        equation_2: float = self.p2.mass * self.ga * math.sin(self.p1.angle - (2 * self.p2.angle))
        equation_3: float = 2 * math.sin(self.p1.angle - self.p2.angle) * self.p2.mass
        equation_4: float = (
                (self.p2.velocity ** 2 * self.p2.length) +
                (self.p1.velocity ** 2 * self.p1.length * math.cos(self.p1.angle - self.p2.angle)))
        denominator_1: float = self.p1.length * (
                (2 * self.p1.mass) + self.p2.mass -
                self.p2.mass * math.cos((2 * self.p1.angle) - (2 * self.p2.angle)))

        self.p1.acceleration = (equation_1 - equation_2 - equation_3 * equation_4) / denominator_1

        return self.p1.acceleration

    def __p2_motion_model(self):
        equation_1: float = 2 * math.sin(self.p1.angle - self.p2.angle)
        equation_2: float = (self.p1.velocity ** 2 * self.p1.length * (self.p1.mass + self.p2.mass))
        equation_3: float = self.ga * (self.p1.mass + self.p2.mass) * math.cos(self.p1.angle)
        equation_4: float = self.p2.velocity ** 2 * self.p2.length * self.p2.mass * math.cos(self.p1.angle - self.p2.angle)
        denominator_2: float = self.p2.length * (2 * self.p1.mass + self.p2.mass - self.p2.mass *
                                              math.cos(2 * self.p1.angle - 2 * self.p2.angle))

        self.p2.acceleration = (equation_1 * (equation_2 + equation_3 + equation_4)) / denominator_2

        return self.p2.acceleration

    def update_motion_model(self):
        self.__p1_motion_model()
        self.__p2_motion_model()

    @staticmethod
    def __draw_pendulum(pendulum: Pendulum, surface: pygame.display, origin: list, end: list):
        pendulum.draw_rod(surface, origin, end)
        pendulum.draw_ball(surface, end)

    def draw(self, surface: pygame.display):
        self.__draw_pendulum(self.p1, surface, self.origin, [self.p1.x, self.p1.y])
        self.__draw_pendulum(self.p2, surface, [self.p1.x, self.p1.y], [self.p2.x, self.p2.y])

    def run_simulation(self, screen: pygame.display):
        self.update_motion_model()
        self.calculate_new_x_y()
        self.update_velocity()
        self.update_angle()
        self.draw(screen)


