# Создание основного окна
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
# Импорт виджетов
from data.base.widgets.MathLayout import MathLayout
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
        up_layout = QGridLayout()  # Делит окно на части
        menu_layout = MenuLayout()  # Часть окна с конфигом
        graph_layout = MathLayout()  # Часть окна с графиком

        up_layout.addLayout(graph_layout, 0, 0)
        up_layout.addLayout(menu_layout, 0, 2)

        # menu_layout.index_changed()

        main_widget = QWidget()
        main_widget.setLayout(up_layout)
        self.setCentralWidget(main_widget)

    @staticmethod
    def render_main_win():
        app = QApplication(sys.argv)

        window = MainWindow(1080, 720)
        window.show()

        app.exec()
