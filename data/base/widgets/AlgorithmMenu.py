from PyQt6.QtCore import Qt, QProcess
from PyQt6.QtWidgets import QVBoxLayout, QComboBox, QPushButton, QLabel, QLineEdit, QHBoxLayout, QPlainTextEdit


class AlgorithmMenu(QVBoxLayout):

    def __init__(self):
        super(AlgorithmMenu, self).__init__()

        # ---------------- ComboBox ---------------- #
        algorithms = ["Градиентный спуск", "Квадратичное программирование", "Функция Розенброкка",
                      "Рой частиц", "Пчелиная оптимизация", "Искусственная имунная сеть",
                      "Бактериальная оптимизация", "Гибридный алгоритм"]
        choose_algorithm = QComboBox()
        choose_algorithm.addItems(algorithms)
        choose_algorithm.currentIndexChanged.connect(self.algorithm_changed)

        self.addWidget(choose_algorithm)

        # ----------------- Labels ----------------- #
        # Разбиение на название - значение
        horizontal_layout = QHBoxLayout()
        vertical_layout_left = QVBoxLayout()
        vertical_layout_right = QVBoxLayout()

        # X
        self.label_x = QLabel('&X')
        self.label_x.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEditX = QLineEdit()
        self.lineEditX.textChanged[str].connect(self.changed)
        self.label_x.setBuddy(self.lineEditX)

        # Y
        self.label_y = QLabel('&Y')
        self.label_y.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEditY = QLineEdit()
        self.lineEditY.textChanged[str].connect(self.changed)
        self.label_y.setBuddy(self.lineEditY)

        # НАЧАЛЬНЫЙ ШАГ
        self.label_first_step = QLabel('&Начальный шаг')
        self.label_first_step.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_first_step = QLineEdit()
        self.lineEdit_first_step.textChanged[str].connect(self.changed)
        self.label_first_step.setBuddy(self.lineEdit_first_step)

        # ЧИСЛО ИТЕРАЦИЙ
        self.label_iterations = QLabel('&Число итераций')
        self.label_iterations.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_iterations = QLineEdit()
        self.lineEdit_iterations.textChanged[str].connect(self.changed)
        self.label_iterations.setBuddy(self.lineEdit_iterations)

        # ЗАДЕРЖКА
        self.label_delay = QLabel('&Задержка')
        self.label_delay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_delay = QLineEdit()
        self.lineEdit_delay.textChanged[str].connect(self.changed)
        self.label_delay.setBuddy(self.lineEdit_delay)

        # Запихиваем в layout
        vertical_layout_left.addWidget(self.label_x)
        vertical_layout_left.addWidget(self.label_y)
        vertical_layout_left.addWidget(self.label_first_step)
        vertical_layout_left.addWidget(self.label_iterations)
        vertical_layout_left.addWidget(self.label_delay)

        vertical_layout_right.addWidget(self.lineEditX)
        vertical_layout_right.addWidget(self.lineEditY)
        vertical_layout_right.addWidget(self.lineEdit_first_step)
        vertical_layout_right.addWidget(self.lineEdit_iterations)
        vertical_layout_right.addWidget(self.lineEdit_delay)

        horizontal_layout.addLayout(vertical_layout_left)
        horizontal_layout.addLayout(vertical_layout_right)

        self.addLayout(horizontal_layout)

        # ---------------- Button ---------------- #
        self.start_button = QPushButton("Выполнить")
        self.start_button.setCheckable(True)
        self.start_button.clicked.connect(self.start_process)

        self.addWidget(self.start_button)

        # --------------- Console --------------- #
        self.p = None  # Значение текущего процесса

        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)

        self.addWidget(self.console)

    def algorithm_changed(self, index):  # i is an int
        print('changed to' + str(index))
        # if index == 1:

    def changed(self, changed_info):
        clear = changed_info.replace(' ', '')
        print(clear)

    # Консольные функции
    def message(self, s):
        self.console.appendPlainText(s)

    def start_process(self):
        if self.p is None:  # Если текущего процесса нет.
            self.message("Executing process")
            self.p = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.p.finished.connect(self.process_finished)  # Очистка процесса.
            self.p.start("python3", ['ourscript.py'])

    def process_finished(self):
        self.message("Process finished.")
        self.p = None
