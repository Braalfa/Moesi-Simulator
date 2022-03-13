import sys
import threading
from enum import Enum

from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5.QtCore import QObject
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
import time
from Cache.cacheL1 import CacheLine
from simulation import Simulation
from CPU.instruction import Instruction


class UpdatesWorker(QObject):
    update_signal = pyqtSignal()
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.continue_flag = True
    
    def run(self):
        while self.continue_flag:
            self.update_signal.emit()
            time.sleep(0.2)
        self.finished.emit()

class WindowsController:
    def __init__(self, simulation: Simulation):
        self.simulation = simulation
        self.qml_path = 'Interface/content/App.qml'
        self.root = None
        self.app = None
        self.continue_button = None
        self.step_button = None
        self.stop_button = None
        self.continue_flag = True
        self.engine = None
        self.update_thread = None
        self.update_worker = None

    def run(self):
        self.app = QGuiApplication(sys.argv)
        self.start_window()
        self.configure_buttons()
        self.start_updates()
        sys.exit(self.app.exec())

    def start_updates(self):
        self.update_thread = QThread()
        self.update_worker = UpdatesWorker()
        self.update_worker.moveToThread(self.update_thread)
        self.update_thread.started.connect(self.update_worker.run)
        self.update_worker.finished.connect(self.update_thread.quit)
        self.update_worker.finished.connect(self.update_worker.deleteLater)
        self.update_thread.finished.connect(self.update_thread.deleteLater)
        self.update_worker.update_signal.connect(self.update_values)
        self.update_thread.start()

    def start_window(self):
        self.engine = QQmlApplicationEngine()
        self.engine.quit.connect(self.app.quit)
        self.engine.load(self.qml_path)
        root_object = self.engine.rootObjects()[0]
        rectangle = root_object.children()[1]
        self.root = rectangle

    def configure_buttons(self):
        self.continue_button = self.root.findChild(QObject, "continue_btn")
        self.step_button = self.root.findChild(QObject, "step_btn")
        self.stop_button = self.root.findChild(QObject, "stop_btn")
        self.setup_buttons()

    def update_values(self):
        for i in range(self.simulation.number_of_cpus):
            instruction_property = "last_execution" + str(i) + "_text"
            current_process_property = "current_process" + str(i) + "_text"
            self.root.setProperty(instruction_property, self.simulation.get_cpu_instruction(i))
            #self.root.setProperty(current_process_property, self.simulation.get_cache_status(i))
            cache_content = self.simulation.get_cache_content(i)
            for j in range(self.simulation.number_of_blocks_per_cache):
                cache_line: CacheLine = cache_content[j]
                data_property = "data" + str(j) + "_" + str(i) + "_text"
                address_property = "address" + str(j) + "_" + str(i) + "_text"
                state_property = "state" + str(j) + "_" + str(i) + "_text"
                self.root.setProperty(data_property, cache_line.data)
                self.root.setProperty(address_property, cache_line.get_address_as_4_bits())
                self.root.setProperty(state_property, cache_line.get_state_as_string())

        memory_contents = self.simulation.get_memory_content()
        for i in range(self.simulation.number_of_memory_lines):
            memory_property = "data_memory" + str(i) + "_text"
            self.root.setProperty(memory_property, memory_contents[i])

    def setup_buttons(self):
        self.continue_button.clicked.connect(self.continue_clicked)
        self.step_button.clicked.connect(self.step_clicked)
        self.stop_button.clicked.connect(self.stop_clicked)

    def continue_clicked(self):
        self.continue_button.setProperty("visible", False)
        self.step_button.setProperty("visible", False)
        self.stop_button.setProperty("visible", True)
        self.assign_next_instruction()
        self.simulation.start_execution()

    def step_clicked(self):
        self.continue_button.setProperty("visible", True)
        self.step_button.setProperty("visible", True)
        self.stop_button.setProperty("visible", False)
        self.assign_next_instruction()
        self.simulation.execute_once()

    def stop_clicked(self):
        self.continue_button.setProperty("visible", True)
        self.step_button.setProperty("visible", True)
        self.stop_button.setProperty("visible", False)
        self.simulation.stop_execution()

    def assign_next_instruction(self):
        input_instruction = self.obtain_input_instruction()
        if input_instruction is not None:
            self.simulation.set_next_instruction(input_instruction)

    def obtain_input_instruction(self) -> Instruction | None:
        instruction_property = "instruction_input_text"
        instruction_string = self.root.property(instruction_property)
        try:
            instruction = Instruction.parse_from_string(instruction_string)
        except:
            instruction = None
        return instruction

    def continue_executing(self):
        sys.exit(self.app.exec())
