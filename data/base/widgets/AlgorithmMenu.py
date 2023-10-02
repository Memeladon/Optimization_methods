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
        choose_algorithm.currentIndexChanged.connect(self.index_changed)

        self.addWidget(choose_algorithm)

        # ----------------- Labels ----------------- #
        # Разбиение на название - значение
        horizontal_layout = QHBoxLayout()
        vertical_layout_left = QVBoxLayout()
        vertical_layout_right = QVBoxLayout()

        # X
        label_x = QLabel('&X')
        label_x.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lineEditX = QLineEdit()
        lineEditX.textChanged[str].connect(self.Changed)
        label_x.setBuddy(lineEditX)

        # Y
        label_y = QLabel('&Y')
        label_y.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lineEditY = QLineEdit()
        lineEditY.textChanged[str].connect(self.Changed)
        label_y.setBuddy(lineEditY)

        # НАЧАЛЬНЫЙ ШАГ
        label_first_step = QLabel('&Начальный шаг')
        label_first_step.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lineEdit_first_step = QLineEdit()
        lineEdit_first_step.textChanged[str].connect(self.Changed)
        label_first_step.setBuddy(lineEdit_first_step)

        # ЧИСЛО ИТЕРАЦИЙ
        label_iterations = QLabel('&Число итераций')
        label_iterations.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lineEdit_iterations = QLineEdit()
        lineEdit_iterations.textChanged[str].connect(self.Changed)
        label_iterations.setBuddy(lineEdit_iterations)

        # ЗАДЕРЖКА
        label_delay = QLabel('&Задержка')
        label_delay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lineEdit_delay = QLineEdit()
        lineEdit_delay.textChanged[str].connect(self.Changed)
        label_delay.setBuddy(lineEdit_delay)

        # Запихиваем в layout
        vertical_layout_left.addWidget(label_x)
        vertical_layout_left.addWidget(label_y)
        vertical_layout_left.addWidget(label_first_step)
        vertical_layout_left.addWidget(label_iterations)
        vertical_layout_left.addWidget(label_delay)

        vertical_layout_right.addWidget(lineEditX)
        vertical_layout_right.addWidget(lineEditY)
        vertical_layout_right.addWidget(lineEdit_first_step)
        vertical_layout_right.addWidget(lineEdit_iterations)
        vertical_layout_right.addWidget(lineEdit_delay)

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

    def index_changed(self, index):  # i is an int
        print('changed to' + str(index))
        # if index == 1:

    def Changed(self, changed_info):
        print(changed_info)

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
