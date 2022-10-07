import pygame

from pendulums.double_pendulum import Pendulum, DoublePendulum
from utils import Colors, MathematicalConstants, Screen, Fonts

pygame.init()
pygame.display.set_caption("Double pendulum")
pygame.font.init()

screen = pygame.display.set_mode(Screen.SCREEN_SIZE)
clock = pygame.time.Clock()

p1 = Pendulum(Colors.BLACK, Colors.RED, 130, 20, 10, MathematicalConstants.PI)
p2 = Pendulum(Colors.BLACK, Colors.RED, 130, 20, 10, MathematicalConstants.PI / 2)

double_pendulum = DoublePendulum(p1, p2, MathematicalConstants.GRAVITY, origin=[Screen.CENTER_WIDTH, Screen.Y_OFFSET])

"""
==== Configurations leading to OverflowError ====

p1 = DoublePendulum(BLACK, RED, 200, 20, 10, PI / 2)
p2 = DoublePendulum(BLACK, RED, 100, 30, 5, PI / 8)

"""


def run():
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(Colors.WHITE)

        double_pendulum.run_simulation(screen)

        font = pygame.font.SysFont(Fonts.STANDARD_FONT, 20)
        display_text = font.render(double_pendulum.p2.get_data('angle'), False, Colors.BLACK, None)
        display_text_2 = font.render(double_pendulum.p2.get_data('y'), False, Colors.BLACK, None)

        screen.blit(display_text, (0, 0))
        screen.blit(display_text_2, (0, 20))

        pygame.display.update()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    run()
