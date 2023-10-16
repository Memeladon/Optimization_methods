from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QLineEdit


class Artificial_immune_network(QHBoxLayout):

    def __init__(self):
        super(Artificial_immune_network, self).__init__()

        horizontal_layout = QHBoxLayout()
        vertical_layout_left = QVBoxLayout()
        vertical_layout_right = QVBoxLayout()

        self.addLayout(horizontal_layout)
