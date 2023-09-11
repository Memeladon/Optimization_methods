from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QComboBox, QPushButton, QLabel


class MenuLayout(QVBoxLayout):

    def __init__(self):
        super(MenuLayout, self).__init__()

        # ---------------- ComboBox ---------------- #
        algorithms = ["Градиентный спуск", "Квадратичное программирование", "Функция Розенброкка",
                      "Рой частиц", "Пчелиная оптимизация", "Искусственная имунная сеть",
                      "Бактериальная оптимизация", "Гибридный алгоритм"]
        choose_algorithm = QComboBox()
        choose_algorithm.addItems(algorithms)
        choose_algorithm.currentIndexChanged.connect(self.index_changed)
        choose_algorithm.currentTextChanged.connect(self.text_changed)

        self.addWidget(choose_algorithm)

        # ---------------- ComboBox ---------------- #
        methods = ["1", "2", "3", "4", "5", "6", "7", "8"]
        choose_methods = QComboBox()
        choose_methods.addItems(methods)
        choose_methods.currentIndexChanged.connect(self.index_changed)
        choose_methods.currentTextChanged.connect(self.text_changed)

        self.addWidget(choose_methods)

        # ---------------- Button ---------------- #
        start_button = QPushButton("Выполнить")
        start_button.setCheckable(True)
        start_button.clicked.connect(self.the_button_was_clicked)

        self.addWidget(start_button)

        # ---------------- Label ---------------- #
        console_out = QLabel("TEXT HERE")
        console_out.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        self.addWidget(console_out)

    def the_button_was_clicked(self):
        print("Clicked!")

    def index_changed(self, i):  # i is an int
        print(i)

    def text_changed(self, s):  # s is a str
        print(s)


