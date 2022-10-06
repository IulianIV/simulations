from abc import ABC, abstractmethod
from typing import Any
import pygame
from utils import Colors, Screen, Fonts

pygame.init()
pygame.font.init()


class Simulation(ABC):

    def __init__(self, screen_size: tuple = Screen.SCREEN_SIZE, name: str = 'Simulation',
                 background: tuple = Colors.WHITE):
        self.clock = pygame.time.Clock()

        self.screen_size = screen_size
        self._screen = self._set_screen()

        self.font_size = self._font_size
        self.font_type = self._font_type

        self.background = background
        pygame.display.set_caption(name)

    def _set_screen(self) -> pygame.display:
        _screen = pygame.display.set_mode(self.screen_size)

        return _screen

    @property
    def _font_size(self):
        size = 10
        return size

    @_font_size.setter
    def _font_size(self, font_size: int):
        self.font_size = font_size

    @property
    def _font_type(self):
        font_type = Fonts.STANDARD_FONT

        return font_type

    @_font_type.setter
    def _font_type(self, font_type: str):
        self.font_type = font_type

    def set_background(self):
        self._screen.fill(self.background)

    def display_data(self, data: Any, txt_antialias: bool = False,
                     txt_color: Any = Colors.BLACK, txt_destination: tuple = (0, 0), txt_background: Any = None):
        font = pygame.font.SysFont(self.font_type, self.font_size)
        display_text = font.render(data, txt_antialias, txt_color, txt_background)
        self._screen.blit(display_text, txt_destination)

    @abstractmethod
    def run(self):
        pass

