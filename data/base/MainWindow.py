# Создание основного окна
import sys
# import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from data.base.widgets.MenuLayout import MenuLayout
from data.base.widgets.TopToolbar import TopToolbar


class MainWindow(QMainWindow):
    def __init__(self, win_w, win_h):
        super(MainWindow, self).__init__()

        # Установка названия окна, иконки и размеров
        self.setWindowTitle("Оптимизационные методы")
        self.setGeometry(100, 100, win_w, win_h)

        # Задержка вывода работы алгоритма для пользователя
        self.output_interval = 0.1

        # Верхнее меню приложения
        self.addToolBar(TopToolbar())

        # Разбиение окна
        up_layout = QGridLayout()
        main_layout = MenuLayout()

        up_layout.addLayout(main_layout, 0, 2)

        widget = QWidget()
        widget.setLayout(up_layout)
        self.setCentralWidget(widget)

    @staticmethod
    def render_main_win():
        app = QApplication(sys.argv)

        window = MainWindow(1080, 720)
        window.show()

        app.exec()
