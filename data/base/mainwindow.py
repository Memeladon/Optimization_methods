# Файл, который запустит наше окно
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget, QComboBox, QLabel,
    QLCDNumber, QProgressBar, QRadioButton, QCheckBox
)


class MainWindow(QMainWindow):
    def __init__(self, win_w, win_h):
        super(MainWindow, self).__init__()

        # Установка названия окна, иконки и размеров
        self.setWindowTitle("Оптимизационные методы")
        # self.setWindowIcon()
        self.setGeometry(100, 100, win_w, win_h)

        # Задержка вывода работы алгоритма для пользователя
        self.output_interval = 0.1

        '''
        #     QComboBox  - Окно выпадающего списка
        #     QLCDNumber  - Довольно неприятный дисплей LCD
        #     QLabel  - Просто метка, не интерактивная
        #     QProgressBar  - Индикатор выполненияx
        #     QPushButton  - Кнопка
        #     QRadioButton  - Переключаемый набор, в котором активен только один элемент
        '''

        # Создание виджета-названия чего-либо в будущем
        name = QLabel("Тут должно быть окно со всей фигней")
        font = name.font()
        font.setPointSize(14)
        name.setFont(font)
        name.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        self.setCentralWidget(name)

        # Виджет выбора алгоритма
        alg_list = QComboBox()
        alg_list.addItems(['Градиентный спуск', 'Следующий метод'])
        alg_list.setMaxCount(8)

        font = alg_list.font()
        font.setPointSize(14)
        alg_list.setFont(font)

        alg_list.currentIndexChanged.connect(self.index_changed)
        alg_list.currentTextChanged.connect(self.text_changed)
        self.setMenuWidget(alg_list)

        # Виджет с выбором варимантов чего-нибудь
        var_check = QCheckBox()
        var_check.setCheckState(Qt.CheckState.Checked)
        var_check.stateChanged.connect(self.show_state)
        self.setCentralWidget(var_check)

    def show_state(self, s):
        print(s == Qt.CheckState.Checked)
        print(s)

    def index_changed(self, i):  # i — это int
        print(i)

    def text_changed(self, s):  # s — это str
        print(s)

    @staticmethod
    def render_window(**kwargs):
        app = QApplication(sys.argv)

        window = MainWindow(1080, 720)
        window.show()

        app.exec()
