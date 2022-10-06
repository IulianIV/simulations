from pendulums.double_pendulum import DoublePendulum, DoublePendulumSimulation
from utils import Colors, MathematicalConstants

p1 = DoublePendulum(Colors.BLACK, Colors.RED, 350, 20, 2, MathematicalConstants.PI / 2)
p2 = DoublePendulum(Colors.BLACK, Colors.RED, 130, 20, 10, MathematicalConstants.PI / 2)


"""
==== Configurations leading to OverflowError ====

p1 = DoublePendulum(BLACK, RED, 200, 20, 10, PI / 2)
p2 = DoublePendulum(BLACK, RED, 100, 30, 5, PI / 8)

"""


if __name__ == '__main__':
    simulate = DoublePendulumSimulation(p1, p2)
    # TODO font size change does not work. Fix that.
    simulate.run()
