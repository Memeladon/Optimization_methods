# Файл, который запустит наше окно
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


# import OpenGL

class MainWindow(QMainWindow):
    def __init__(self, win_w, win_h):
        super().__init__()

        self.setWindowTitle("Оптимизационные методы")
        # self.setWindowIcon()
        self.setGeometry(100, 100, win_w, win_h)
        button = QPushButton("Press Me!")

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(button)
        self.Output_interval = 0.1


def render():
    app = QApplication(sys.argv)

    window = MainWindow(1080, 720)
    window.show()

    app.exec()
