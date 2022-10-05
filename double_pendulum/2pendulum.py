import pygame
import math
from pendulum import DoublePendulum, PI
from utils import SCREEN_SIZE, BLACK, RED, GRAVITY, WHITE, CENTER_WIDTH, Y_OFFSET

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
trace_screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Double pendulum")

clock = pygame.time.Clock()

p1 = DoublePendulum(BLACK, RED, 200, 20, 10, PI / 2)
p2 = DoublePendulum(BLACK, RED, 100, 30, 5, PI / 8)


"""
==== Configurations leading to OverflowError ====

p1 = DoublePendulum(BLACK, RED, 200, 20, 10, PI / 2)
p2 = DoublePendulum(BLACK, RED, 100, 30, 5, PI / 8)

"""


def run_pendulum():
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)
        trace_screen.fill(WHITE)

        p1.p1_motion_model(GRAVITY, p2)
        p2.p2_motion_model(GRAVITY, p1)

        # implement the update_y function
        p1.x = p1.length * math.sin(p1.angle) + CENTER_WIDTH
        p1.y = p1.length * math.cos(p1.angle) + Y_OFFSET

        p2.x = p1.x + p2.length * math.sin(p2.angle)
        p2.y = p1.y + p2.length * math.cos(p2.angle)

        """
        ===== DRAW SECTION ====
        """

        p1.draw(screen, [CENTER_WIDTH, Y_OFFSET], [p1.x, p1.y])
        p2.draw(screen, [p1.x, p1.y], [p2.x, p2.y])

        p1.velocity += p1.acceleration
        p2.velocity += p2.acceleration
        p1.angle += p1.velocity
        p2.angle += p2.velocity

        pygame.display.update()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    run_pendulum()
