from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QComboBox, QPushButton, QLabel, QLineEdit, QHBoxLayout


class FunctionsMenu(QVBoxLayout):

    def __init__(self):
        super(FunctionsMenu, self).__init__()

        # ---------------- ComboBox ---------------- #
        methods = ["Функция Химмельблау", "2", "3", "4", "5", "6", "7", "8"]
        choose_methods = QComboBox()
        choose_methods.addItems(methods)
        choose_methods.currentIndexChanged.connect(self.index_changed)

        self.addWidget(choose_methods)

        # ---------------- Label ---------------- #
        # Разбиение на название - значение
        horizontal_layout = QHBoxLayout()
        vertical_layout_left = QVBoxLayout()
        vertical_layout_right = QVBoxLayout()

        # (X0;X1)
        label_x = QLabel('&X интервал')
        label_x.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lineEditX = QLineEdit()
        lineEditX.textChanged[str].connect(self.Changed)
        label_x.setBuddy(lineEditX)

        # (Y0;Y1)
        label_y = QLabel('&Y интервал')
        label_y.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lineEditY = QLineEdit()
        lineEditY.textChanged[str].connect(self.Changed)
        label_y.setBuddy(lineEditY)

        # Z МАСШТАБ
        label_z = QLabel('&Z масштаб')
        label_z.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lineEditZ = QLineEdit()
        lineEditZ.textChanged[str].connect(self.Changed)
        label_z.setBuddy(lineEditZ)

        # # ОСЬ
        # label_osx = QLabel('&Ось X интервал')
        # label_osx.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # lineEditOSX = QLineEdit()
        # lineEditOSX.textChanged[str].connect(self.Changed)
        # label_osx.setBuddy(lineEditOSX)
        #
        # # ОСЬ
        # label_osy = QLabel('&Ось Y интервал')
        # label_osy.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # lineEditOSY = QLineEdit()
        # lineEditOSY.textChanged[str].connect(self.Changed)
        # label_osy.setBuddy(lineEditOSY)

        # Запихиваем в layout
        vertical_layout_left.addWidget(label_x)
        vertical_layout_left.addWidget(label_y)
        vertical_layout_left.addWidget(label_z)
        # vertical_layout_left.addWidget(label_osx)
        # vertical_layout_left.addWidget(label_osy)

        vertical_layout_right.addWidget(lineEditX)
        vertical_layout_right.addWidget(lineEditY)
        vertical_layout_right.addWidget(lineEditZ)
        # vertical_layout_right.addWidget(lineEditOSX)
        # vertical_layout_right.addWidget(lineEditOSY)

        horizontal_layout.addLayout(vertical_layout_left)
        horizontal_layout.addLayout(vertical_layout_right)

        self.addLayout(horizontal_layout)

    def index_changed(self, index):  # i is an int
        print(index)
        # if index == 1:
            
    def Changed(self, changed_info):
        print(changed_info)




