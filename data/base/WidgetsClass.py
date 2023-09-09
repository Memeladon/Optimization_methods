from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor, QAction, QIcon
from PyQt6.QtWidgets import QWidget, QComboBox, QLabel, QPushButton, QVBoxLayout, QToolBar


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


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


class TopToolbar(QToolBar):
    def __init__(self):
        super(QToolBar, self).__init__()

        self.setIconSize(QSize(16, 16))
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        button_action = QAction(QIcon("data/icon.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        self.addAction(button_action)
        self.addSeparator()

        button_action2 = QAction(QIcon("data/icon.png"), "&Your button", self)
        button_action2.setStatusTip("This is your button")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)

        self.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)
