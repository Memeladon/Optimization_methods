from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit


class Rosenbrock_function(QHBoxLayout):

    def __init__(self):
        super(Rosenbrock_function, self).__init__()

        horizontal_layout = QHBoxLayout()
        vertical_layout_left = QVBoxLayout()
        vertical_layout_right = QVBoxLayout()

        self.addLayout(horizontal_layout)
