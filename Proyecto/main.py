import threading
from simulation import Simulation
from Interface.window import WindowsController


def main():
    simulation = Simulation()
    simulation.execute()
    window_controller = WindowsController(simulation)
    window_controller.run()


if __name__ == '__main__':
    main()
