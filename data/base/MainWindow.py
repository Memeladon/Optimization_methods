# Создание основного окна
import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout

# Импорт виджетов
from data.base.widgets.AlgorithmMenu import AlgorithmMenu
from data.base.widgets.FunctionsMenu import FunctionsMenu
from data.base.widgets.MathLayout import MathLayout
from data.base.widgets.TopToolbar import TopToolbar


class MainWindow(QMainWindow):
    def __init__(self, win_w, win_h):
        super(MainWindow, self).__init__()

        # Установка названия окна, иконки и размеров
        self.setWindowTitle("Оптимизационные методы")
        self.setWindowIcon(QtGui.QIcon('data/images/app.png'))
        self.setGeometry(100, 100, win_w, win_h)

        # Верхнее меню приложения
        self.addToolBar(TopToolbar())

        # Разбиение окна
        main_layout = QGridLayout()  # Делит окно на части (в нашем случае на 2)
        right_layout = QVBoxLayout()  # Правая часть окна
        left_layout = MathLayout()  # Левая чать окна (часть окна с графиком)

        # Задается правая часть (Меню)
        functions_menu = FunctionsMenu()
        algorithm_menu = AlgorithmMenu()  # Часть окна с конфигом

        right_layout.addLayout(algorithm_menu)
        right_layout.addLayout(functions_menu)

        # Добавление частей в окно
        main_layout.addLayout(left_layout, 0, 0)
        main_layout.addLayout(right_layout, 0, 1)

        # functions_menu.function_changed()

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    @staticmethod
    def render_main_win():
        app = QApplication(sys.argv)

        window = MainWindow(1080, 720)
        window.show()

        app.exec()
