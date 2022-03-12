import threading
from simulation import Simulation
from Interface.window import WindowsController


def main():
    simulation = Simulation()
    simulation.execute()
    window_controller = WindowsController(simulation)
    thread = threading.Thread(target=window_controller.start_window, args=())
    thread.start()
    thread.join()


if __name__ == '__main__':
    main()
