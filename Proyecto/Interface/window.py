import sys
import threading

from PyQt5.QtCore import QVariant
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
import time
from PyQt5.QtQuick import QQuickItem

def function(engine):
    root_object = engine.rootObjects()[0]
    rectangle = root_object.children()[1]

    for i in range(4):
        instruction_property = "last_execution" + str(i) + "_text"
        current_process_property = "current_process" + str(i) + "_text"
        rectangle.setProperty(instruction_property, QVariant("instruction"))
        # read input
        # print(rectangle.property("last_execution1_text"))
        rectangle.setProperty(current_process_property, QVariant("idle"))
        for j in range(4):
            data_property = "data" + str(j) + "_" + str(i) + "_text"
            address_property = "address" + str(j) + "_" + str(i) + "_text"
            state_property = "state" + str(j) + "_" + str(i) + "_text"
            rectangle.setProperty(data_property, QVariant("abcd"))
            rectangle.setProperty(address_property, QVariant("1010"))
            rectangle.setProperty(state_property, QVariant("I"))

    for i in range(16):
        memory_property = "data_memory" + str(i) + "_text"
        rectangle.setProperty(memory_property, QVariant(str(i)))


app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('content/App.qml')

function(engine)

sys.exit(app.exec())
