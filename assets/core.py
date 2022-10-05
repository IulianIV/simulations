from abc import ABC, abstractmethod
import pygame

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()


class Simulation(ABC):

    def __init__(self, screen_size: tuple = (1000, 1000), name: str = 'Simulation',
                 font: str = 'Times New Roman'):
        self.screen_size = screen_size
        self._screen = self._set_screen()
        self._font = self.font_size
        self.font = pygame.font.SysFont(font, self._font)
        pygame.display.set_caption(name)

    def _set_screen(self) -> pygame.display:
        _screen = pygame.display.set_mode(self.screen_size)

        return _screen

    @property
    def font_size(self):
        font_size = 10
        return font_size

    @font_size.setter
    def font_size(self, font_size: int):
        self._font = font_size

    @abstractmethod
    def run(self):
        pass

