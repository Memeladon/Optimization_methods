from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit


class Gradient_descent(QHBoxLayout):
    data_changed = pyqtSignal(float, float, float, float, float,)

    def __init__(self):
        super(Gradient_descent, self).__init__()

        grid_layout = QGridLayout()

        # horizontal_layout = QHBoxLayout()
        # vertical_layout_left = QVBoxLayout()
        # vertical_layout_right = QVBoxLayout()

        # X
        self.label_x = QLabel('&X')
        self.label_x.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditX = QLineEdit('-1')
        self.lineEditX.textChanged[str].connect(self.x_alg)
        self.label_x.setBuddy(self.lineEditX)

        # Y
        self.label_y = QLabel('&Y')
        self.label_y.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEditY = QLineEdit('-1')
        self.lineEditY.textChanged[str].connect(self.y_alg)
        self.label_y.setBuddy(self.lineEditY)

        # НАЧАЛЬНЫЙ ШАГ
        self.label_first_step = QLabel('&Начальный шаг')
        self.label_first_step.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_first_step = QLineEdit('0.5')
        self.lineEdit_first_step.textChanged[str].connect(self.step_alg)
        self.label_first_step.setBuddy(self.lineEdit_first_step)

        # ЧИСЛО ИТЕРАЦИЙ
        self.label_iterations = QLabel('&Число итераций')
        self.label_iterations.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_iterations = QLineEdit('100')
        self.lineEdit_iterations.textChanged[str].connect(self.iter_alg)
        self.label_iterations.setBuddy(self.lineEdit_iterations)

        # ЗАДЕРЖКА
        self.label_delay = QLabel('&Задержка')
        self.label_delay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_delay = QLineEdit('0.5')
        self.lineEdit_delay.textChanged[str].connect(self.changed)
        self.label_delay.setBuddy(self.lineEdit_delay)

        # Запихиваем в layout
        # vertical_layout_left.addWidget(self.label_x)
        # vertical_layout_left.addWidget(self.label_y)
        # vertical_layout_left.addWidget(self.label_first_step)
        # vertical_layout_left.addWidget(self.label_iterations)
        # vertical_layout_left.addWidget(self.label_delay)
        #
        # vertical_layout_right.addWidget(self.lineEditX)
        # vertical_layout_right.addWidget(self.lineEditY)
        # vertical_layout_right.addWidget(self.lineEdit_first_step)
        # vertical_layout_right.addWidget(self.lineEdit_iterations)
        # vertical_layout_right.addWidget(self.lineEdit_delay)
        #
        # horizontal_layout.addLayout(vertical_layout_left)
        # horizontal_layout.addLayout(vertical_layout_right)

        grid_layout.addWidget(self.label_x, 0, 0)
        grid_layout.addWidget(self.lineEditX, 0, 1)
        grid_layout.addWidget(self.label_y, 1, 0)
        grid_layout.addWidget(self.lineEditY, 1, 1)
        grid_layout.addWidget(self.label_first_step, 2, 0)
        grid_layout.addWidget(self.label_iterations, 3, 0)
        grid_layout.addWidget(self.label_delay, 4, 0)
        grid_layout.addWidget(self.lineEdit_first_step, 2, 1)
        grid_layout.addWidget(self.lineEdit_iterations, 3, 1)
        grid_layout.addWidget(self.lineEdit_delay, 4, 1)

        self.addLayout(grid_layout)

    def changed(self, changed_info):
        clear = changed_info.replace(' ', '')
        print(clear)

    # Функция обрабатывающая изменения в строке алгоритмов (X)
    def x_alg(self):
        clear = self.lineEditX.text().replace('(', '').replace(')', '').replace(' ', '').replace(';', ' ')
        xs = clear.split()
        print('X:' + str(xs))
        return xs

    # Функция обрабатывающая изменения в строке алгоритмов (Y)
    def y_alg(self):
        clear = self.lineEditY.text().replace('(', '').replace(')', '').replace(' ', '').replace(';', ' ')
        ys = clear.split()
        print('Y:' + str(ys))
        return ys

    # Функция обрабатывающая изменения в строке алгоритмов (Steps)
    def step_alg(self):
        clear = self.lineEdit_first_step.text().replace(' ', '').replace(',', '.')
        print('Начальный шаг:' + str(clear))
        return clear

    # Функция обрабатывающая изменения в строке алгоритмов (Iterations)
    def iter_alg(self):
        clear = self.lineEdit_iterations.text().replace(' ', '')
        print('Число итераций:' + str(clear))
        return clear

    # Функция обрабатывающая изменения в строке алгоритмов (Delay)
    def delay_alg(self):
        clear = self.lineEdit_delay.text().replace(' ', '').replace(',', '.')
        print('Задержка:' + str(clear))
        return clear

    def collect_data_layout(self):
        x = self.x_alg()
        y = self.y_alg()
        first_step = self.step_alg()
        amount_iter = self.iter_alg()
        delay = self.delay_alg()

        self.data_changed.emit(x, y, first_step, amount_iter, delay)



