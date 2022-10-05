import pygame
from assets.core import Simulation
from pendulum import DoublePendulum, PI
from utils import SCREEN_SIZE, BLACK, RED, GRAVITY, WHITE, CENTER_WIDTH, Y_OFFSET

pygame.init()

# pendulum_font = pygame.font.SysFont('Times New Roman', 18)
#
# screen = pygame.display.set_mode(SCREEN_SIZE)
#
# pygame.display.set_caption("Double pendulum")
#
# clock = pygame.time.Clock()

p1 = DoublePendulum(BLACK, RED, 350, 20, 2, PI / 2)
p2 = DoublePendulum(BLACK, RED, 130, 20, 10, PI / 2)


"""
==== Configurations leading to OverflowError ====

p1 = DoublePendulum(BLACK, RED, 200, 20, 10, PI / 2)
p2 = DoublePendulum(BLACK, RED, 100, 30, 5, PI / 8)

"""

class PendulumSimulation(Simulation):

    def __init__(self):
        super().__init__()
        pass


def run_pendulum():
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)

        p1.p1_motion_model(GRAVITY, p2)
        p2.p2_motion_model(GRAVITY, p1)

        # implement the calculate_new_y function
        p1.calculate_new_x(CENTER_WIDTH)
        p1.calculate_new_y(Y_OFFSET)

        p2.calculate_new_x(pendulum=p1)
        p2.calculate_new_y(pendulum=p1)

        p1.update_velocity()
        p2.update_velocity()

        p1.update_angle()
        p2.update_angle()

        """
        ===== DRAW SECTION ====
        """

        display_text = pendulum_font.render(p1.get_data('x'), False, (0, 0, 0))
        screen.blit(display_text, (0, 0))



        p1.draw(screen, [CENTER_WIDTH, Y_OFFSET], [p1.x, p1.y])
        p2.draw(screen, [p1.x, p1.y], [p2.x, p2.y])

        pygame.display.update()

        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    run_pendulum()
