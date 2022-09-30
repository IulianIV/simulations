import pygame
import math
from pendulum import Pendulum, PI
from utils import SCREEN_SIZE, BLACK, RED, GRAVITY, WHITE, CENTER_WIDTH, Y_OFFSET

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
trace_screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption("Double pendulum")

done = False

clock = pygame.time.Clock()

p1 = Pendulum(BLACK, RED, 200, 20, 10, PI / 8)
p2 = Pendulum(BLACK, RED, 200, 20, 10, PI)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    trace_screen.fill(WHITE)

    sub_eq1_1: float = - GRAVITY * ((2 * p1.mass) + p2.mass) * math.sin(p1.angle)
    sub_eq1_2: float = p2.mass * GRAVITY * math.sin(p1.angle - (2 * p2.angle))
    sub_eq1_3: float = 2 * math.sin(p1.angle - p2.angle) * p2.mass
    sub_eq1_4: float = ((p2.velocity**2 * p2.length) + (p1.velocity**2 * p1.length * math.cos(p1.angle - p2.angle)))
    denominator_1: float = p1.length * ((2 * p1.mass) + p2.mass - p2.mass * math.cos((2 * p1.angle) - (2 * p2.angle)))

    p1.acceleration = (sub_eq1_1 - sub_eq1_2 - sub_eq1_3 * sub_eq1_4) / denominator_1

    sub_eq2_1: float = 2 * math.sin(p1.angle - p2.angle)
    sub_eq2_2: float = (p1.velocity**2 * p1.length * (p1.mass + p2.mass))
    sub_eq2_3: float = GRAVITY * (p1.mass + p2.mass) * math.cos(p1.angle)
    sub_eq2_4: float = p2.velocity**2 * p2.length * p2.mass * math.cos(p1.angle - p2.angle)
    denominator_2: float = p2.length * (2 * p1.mass + p2.mass - p2.mass * math.cos(2 * p1.angle - 2 * p2.angle))

    p2.acceleration = (sub_eq2_1 * (sub_eq2_2 + sub_eq2_3 + sub_eq2_4)) / denominator_2

    p1.x = p1.length * math.sin(p1.angle) + CENTER_WIDTH
    p1.y = p1.length * math.cos(p1.angle) + Y_OFFSET

    p2.x = p1.x + p2.length * math.sin(p2.angle)
    p2.y = p1.y + p2.length * math.cos(p2.angle)

    p1.draw(screen, [CENTER_WIDTH, Y_OFFSET], [p1.x, p1.y])
    p2.draw(screen, [p1.x, p1.y], [p2.x, p2.y])

    p1.velocity += p1.acceleration
    p2.velocity += p2.acceleration
    p1.angle += p1.velocity
    p2.angle += p2.velocity

    pygame.display.update()

    clock.tick(60)

pygame.quit()
