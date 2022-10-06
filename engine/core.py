from abc import ABC, abstractmethod
import pygame
from utils import Colors, Screen, Fonts

pygame.init()
pygame.font.init()


class Simulation(ABC):

    def __init__(self, screen_size: tuple = Screen.SCREEN_SIZE, name: str = 'Simulation',
                 font: str = Fonts.STANDARD_FONT, background: tuple = Colors.WHITE):
        self.clock = pygame.time.Clock()
        self.screen_size = screen_size
        self._screen = self._set_screen()
        self._font_size = 10
        self.font = pygame.font.SysFont(font, self._font_size)
        self.background = background
        pygame.display.set_caption(name)

    def _set_screen(self) -> pygame.display:
        _screen = pygame.display.set_mode(self.screen_size)

        return _screen

    def font_size(self, font_size: int):
        self._font_size = font_size

    def set_background(self):
        self._screen.fill(self.background)

    @abstractmethod
    def run(self):
        pass

