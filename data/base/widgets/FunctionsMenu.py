from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QVBoxLayout, QComboBox, QLabel, QLineEdit, QHBoxLayout, QPushButton


class FunctionsMenu(QVBoxLayout):
    # Дата, которую мы отправляем
    data_changed = pyqtSignal(list, list, str, int)
    func_name = pyqtSignal(str)

    def __init__(self):
        super(FunctionsMenu, self).__init__()

        # ---------------- ComboBox ---------------- #
        methods = ["Функция Химмельблау", "Функция сферы", "Функция Матьяса", "Функция Изома", "Функция Экли",
                   "Табличная функция Хольдера"]
        self.choose_methods = QComboBox()
        self.choose_methods.addItems(methods)
        self.choose_methods.currentTextChanged.connect(self.function_changed)

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

        # КНОПКА ОБНОВЛЕНИЯ CANVAS
        self.update_button = QPushButton("Обновить")
        self.update_button.clicked.connect(self.update_canvas_button)

        self.addWidget(self.update_button)

    # Функция отправляющая данные функционального меню в отрисовку canvas
    def update_canvas_button(self):  # i is an int
        x_intervals = self.x_changed_intervals()
        y_intervals = self.y_changed_intervals()
        scale = self.changed_scale()
        selected_function = self.choose_methods.currentIndex()

        # Отправьте данные через сигнал
        self.data_changed.emit(x_intervals, y_intervals, scale, selected_function)

    # Функция обрабатывающая изменения в строке функций (Интервал Х)
    def x_changed_intervals(self):
        clear = self.lineEditX.text().replace('(', '').replace(')', '').replace(' ', '').replace(';', ' ')
        xs = clear.split()
        print('X интервал:' + str(xs))
        return xs

    # Функция обрабатывающая изменения в строке функций (Интервал Y)
    def y_changed_intervals(self):
        clear = self.lineEditY.text().replace('(', '').replace(')', '').replace(' ', '').replace(';', ' ')
        ys = clear.split()
        print('Y интервал:' + str(ys))
        return ys

    # Функция обрабатывающая изменения в строке функций (Масштаб Z)
    def changed_scale(self):
        clear = self.lineEditZ.text().replace(' ', '').replace(';', ' ')
        print('Z масштаб:' + clear)
        return clear

    # Функция задает начатьльное отображение в canvas
    def set_initial_values(self):
        # Устанавливаем первую функцию из списка
        self.choose_methods.setCurrentIndex(0)
        # Вызываем метод для обновления canvas
        self.func_name.emit(self.choose_methods.currentText())
        self.update_canvas_button()

    def function_changed(self, name):
        if name == 'Табличная функция Хольдера' or 'Функция Экли':
            self.lineEditX.setText('(-10;10)')
            self.lineEditY.setText('(-10;10)')
        else:
            self.lineEditX.setText('(-5;5)')
            self.lineEditY.setText('(-5;5)')

        self.func_name.emit(name)
