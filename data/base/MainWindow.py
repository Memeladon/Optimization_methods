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
        self.main_layout = QGridLayout()  # Делит окно на части (в нашем случае на 2)
        self.right_layout = QVBoxLayout()  # Правая часть окна

        # Задается правая часть (Меню)
        self.functions_menu = FunctionsMenu()

        # Левая чать окна (часть окна с графиком)
        self.left_layout = MathLayout()
        self.functions_menu.data_changed.connect(self.left_layout.update_canvas)

        # Правая часть окна (часть с настройками)
        self.algorithm_menu = AlgorithmMenu(self.left_layout)
        self.functions_menu.func_name.connect(self.algorithm_menu.change_func)

        self.right_layout.addLayout(self.algorithm_menu)
        self.right_layout.addLayout(self.functions_menu)

        # Добавление частей в окно
        self.main_layout.addLayout(self.left_layout, 0, 0)
        self.main_layout.addLayout(self.right_layout, 0, 1)

        # functions_menu.function_changed()

        main_widget = QWidget()
        main_widget.setLayout(self.main_layout)
        self.setCentralWidget(main_widget)

    @staticmethod
    def render_main_win():
        app = QApplication(sys.argv)

        window = MainWindow(1080, 720)
        window.show()

        # Вызываем set_initial_values для FunctionsMenu
        window.functions_menu.set_initial_values()

        app.exec()
