from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QComboBox, QLabel, QLineEdit, QHBoxLayout

from data.base.widgets.MathLayout import MathLayout


class FunctionsMenu(QVBoxLayout):

    def __init__(self):
        super(FunctionsMenu, self).__init__()

        # ---------------- ComboBox ---------------- #
        methods = ["Функция Химмельблау", "2", "3", "4", "5", "6", "7", "8"]
        self.choose_methods = QComboBox()
        self.choose_methods.addItems(methods)
        self.choose_methods.currentIndexChanged.connect(self.function_changed)

        self.addWidget(self.choose_methods)

        # ----------------- Label ----------------- #
        # Разбиение на название - значение
        horizontal_layout = QHBoxLayout()
        vertical_layout_left = QVBoxLayout()
        vertical_layout_right = QVBoxLayout()

        # (X0;X1)
        self.label_x = QLabel('&X интервал')
        self.label_x.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEditX = QLineEdit('(-5;5)')
        self.lineEditX.textChanged[str].connect(self.x_changed_intervals)
        self.label_x.setBuddy(self.lineEditX)

        # (Y0;Y1)
        self.label_y = QLabel('&Y интервал')
        self.label_y.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEditY = QLineEdit('(-5;5)')
        self.lineEditY.textChanged[str].connect(self.y_changed_intervals)
        self.label_y.setBuddy(self.lineEditY)

        # Z МАСШТАБ
        self.label_z = QLabel('&Z масштаб')
        self.label_z.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEditZ = QLineEdit('1')
        self.lineEditZ.textChanged[str].connect(self.changed_scale)
        self.label_z.setBuddy(self.lineEditZ)

        # # ОСЬ
        # label_osx = QLabel('&Ось X интервал')
        # label_osx.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # lineEditOSX = QLineEdit()
        # lineEditOSX.textChanged[str].connect(self.changed_intervals)
        # label_osx.setBuddy(lineEditOSX)
        #
        # # ОСЬ
        # label_osy = QLabel('&Ось Y интервал')
        # label_osy.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        # lineEditOSY = QLineEdit()
        # lineEditOSY.textChanged[str].connect(self.changed_intervals)
        # label_osy.setBuddy(lineEditOSY)

        # Запихиваем в layout
        vertical_layout_left.addWidget(self.label_x)
        vertical_layout_left.addWidget(self.label_y)
        vertical_layout_left.addWidget(self.label_z)
        # vertical_layout_left.addWidget(label_osx)
        # vertical_layout_left.addWidget(label_osy)

        vertical_layout_right.addWidget(self.lineEditX)
        vertical_layout_right.addWidget(self.lineEditY)
        vertical_layout_right.addWidget(self.lineEditZ)
        # vertical_layout_right.addWidget(lineEditOSX)
        # vertical_layout_right.addWidget(lineEditOSY)

        horizontal_layout.addLayout(vertical_layout_left)
        horizontal_layout.addLayout(vertical_layout_right)

        self.addLayout(horizontal_layout)

    # Функция обрабатывающая выбор функций
    def function_changed(self, index):  # i is an int
        MathLayout.update_canvas(index)
        # print(index)

    # Функция обрабатывающая изменения в строке функций (Интервал Х)
    def x_changed_intervals(self):
        clear = self.lineEditX.text().replace('(', '').replace(')', '').replace(' ', '').replace(';', ' ')
        xs = clear.split()
        print('X интервал:' + str(xs))
        return xs

    # Функция обрабатывающая изменения в строке функций (Интервал Y)
    def y_changed_intervals(self):
        clear = self.lineEditX.text().replace('(', '').replace(')', '').replace(' ', '').replace(';', ' ')
        ys = clear.split()
        print('Y интервал:' + str(ys))
        return ys

    # Функция обрабатывающая изменения в строке функций (Масштаб Z)
    def changed_scale(self):
        clear = self.lineEditZ.text().replace(' ', '').replace(';', ' ')
        print(clear)
        return clear
