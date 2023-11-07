from PyQt6.QtCore import QProcess, pyqtSignal, pyqtSlot, Qt
from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QComboBox, QPushButton, QPlainTextEdit, QStackedLayout, QLabel,
                             QLineEdit, QGridLayout)

from data.base.layouts import (Artificial_immune_network, Bacterial_optimization, Bee_optimization, Gradient_descent,
                               Hybrid_algorithm, Quadratic_programming, Rosenbrock_function, Swarm_of_particles)

from data.algorithms import (gradient_descent)

from data.functions import (HolderTableFunction, Himmelblau, SphereFunction, MathiasFunction, IzomaFunction,
                            AckleyFunction)


class AlgorithmMenu(QVBoxLayout):
    data_changed = pyqtSignal(list)
    function = 'Функция Химмельблау'

    def __init__(self, math_layout):
        super(AlgorithmMenu, self).__init__()
        self.math_layout = math_layout
        #
        # # ---------------- ComboBox ---------------- #
        algorithms = ["Градиентный спуск", "Квадратичное программирование", "Функция Розенброкка",
                      "Рой частиц", "Пчелиная оптимизация", "Искусственная имунная сеть",
                      "Бактериальная оптимизация", "Гибридный алгоритм"]
        self.choose_algorithm = QComboBox()
        self.choose_algorithm.addItems(algorithms)
        # self.choose_algorithm.currentIndexChanged.connect(self.algorithm_changed)
        self.addWidget(self.choose_algorithm)

        self.functions_dict = {
            "Функция Химмельблау": Himmelblau.objective,
            "Функция сферы": SphereFunction.objective,
            "Функция Матьяса": MathiasFunction.objective,
            "Функция Изома": IzomaFunction.objective,
            "Функция Экли": AckleyFunction.objective,
            "Табличная функция Хольдера": HolderTableFunction.objective,
        }

        # # Словарь слоев
        # self.layout_dict = {
        #     "Градиентный спуск": Gradient_descent.Gradient_descent(),
        #     "Квадратичное программирование": Quadratic_programming.Quadratic_programming(),
        #     "Функция Розенброкка": Rosenbrock_function.Rosenbrock_function(),
        #     "Рой частиц": Swarm_of_particles.Swarm_of_particles(),
        #     "Пчелиная оптимизация": Bee_optimization.Bee_optimization(),
        #     "Искусственная имунная сеть": Artificial_immune_network.Artificial_immune_network(),
        #     "Бактериальная оптимизация": Bacterial_optimization.Bacterial_optimization(),
        #     "Гибридный алгоритм": Hybrid_algorithm.Hybrid_algorithm()
        # }

        # # ----------------- Labels ----------------- #

        # self.stacked_layout = QStackedLayout()

        # # QStackedLayout управляет виджетами, а не макетами напрямую;
        # for layout in self.layout_dict.values():
        #     widget = QWidget()
        #     widget.setLayout(layout)
        #     self.stacked_layout.addWidget(widget)

        # self.addLayout(self.stacked_layout)

        grid_layout = QGridLayout()

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

        # ----------------- Delay ----------------- #
        self.label_delay = QLabel('&Задержка')
        self.label_delay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_delay = QLineEdit('0.5')
        self.lineEdit_delay.textChanged[str].connect(self.delay_alg)
        self.label_delay.setBuddy(self.lineEdit_delay)

        grid_layout.addWidget(self.label_x, 0, 0)
        grid_layout.addWidget(self.lineEditX, 0, 1)

        grid_layout.addWidget(self.label_y, 1, 0)
        grid_layout.addWidget(self.lineEditY, 1, 1)

        grid_layout.addWidget(self.label_delay, 2, 1)
        grid_layout.addWidget(self.lineEdit_delay, 2, 1)

        grid_layout.addWidget(self.label_first_step, 3, 0)
        grid_layout.addWidget(self.lineEdit_first_step, 3, 1)

        grid_layout.addWidget(self.label_iterations, 4, 0)
        grid_layout.addWidget(self.lineEdit_iterations, 4, 1)

        self.addLayout(grid_layout)

        # ---------------- Button ---------------- #
        self.start_button = QPushButton("Выполнить")
        self.start_button.setCheckable(True)
        self.start_button.clicked.connect(self.start_process)

        self.addWidget(self.start_button)

        # --------------- Console --------------- #
        self.process = None  # Значение текущего процесса

        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)

        self.addWidget(self.console)

        # self.layout_dict["Градиентный спуск"].data_out.connect(self.collect_data)

    # Функция обрабатывающая выбор алгоритмов
    # def algorithm_changed(self, index):  # i is an int
    #     # print('changed to ' + str(index))
    #     algorithm_name = self.choose_algorithm.itemText(index)
    #     layout = self.layout_dict.get(algorithm_name)
    #
    #     # Получим индекс виджета, который содержит необходимый layout (макет)
    #     if layout:
    #         index_widget = self.stacked_layout.indexOf(layout.parentWidget())
    #         self.stacked_layout.setCurrentIndex(index_widget)
    #     else:
    #         print("Реализация алгоритма не найдена!")
    #     # if index == 0:

    # Консольные функции

    # Функция обрабатывающая изменения в строке алгоритмов (Delay)
    def delay_alg(self):
        clear = self.lineEdit_delay.text().replace(' ', '').replace(',', '.')
        print('Задержка:' + str(clear))
        return clear

    # Функция обрабатывающая изменения в строке алгоритмов (X)
    def x_alg(self):
        clear = self.lineEditX.text().replace(' ', '')
        print('X:' + str(clear))
        return clear

    # Функция обрабатывающая изменения в строке алгоритмов (Y)
    def y_alg(self):
        clear = self.lineEditY.text().replace(' ', '').replace(',', '.')
        print('Y:' + str(clear))
        return clear

    # Функция обрабатывающая изменения в строке алгоритмов (Steps)
    def step_alg(self):
        clear = self.lineEdit_first_step.text().replace(' ', '').replace(',', '.')
        print('Начальный шаг:' + str(clear))
        return clear

    # Функция обрабатывающая изменения в строке алгоритмов (Iterations)
    def iter_alg(self):
        clear = self.lineEdit_iterations.text().replace(' ', '').replace(',', '.')
        print('Число итераций:' + str(clear))
        return clear

    def message(self, s):
        self.console.appendPlainText(s)

    def start_process(self):
        if self.process is None:  # Если текущего процесса нет.
            # data = self.collect_data()

            x = self.x_alg()
            y = self.y_alg()
            tk = self.step_alg()  # Начальный шаг
            M = self.iter_alg()  # Количество итераций
            alg_name = self.choose_algorithm.currentText()  # Название текущего алгоритма

            self.message(f"Выполнение алготима: {alg_name}.")
            self.process = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.

            if alg_name == "Градиентный спуск":
                result = gradient_descent(self.functions_dict[self.function], x, y, tk, M)
            elif alg_name == "Квадратичное программирование":
                result = None
            elif alg_name == "Функция Розенброкка":
                result = None
            elif alg_name == "Рой частиц":
                result = None
            elif alg_name == "Пчелиная оптимизация":
                result = None
            elif alg_name == "Искусственная имунная сеть":
                result = None
            elif alg_name == "Бактериальная оптимизация":
                result = None
            elif alg_name == "Гибридный алгоритм":
                result = None

            self.process.finished.connect(self.process_finished)  # Очистка процесса.

            # self.process.start("python3", ['gradient_descent.py'])
            # self.process_finished()

    def process_finished(self):
        self.message("Конец выполнения.")
        self.process = None

    @pyqtSlot(str)
    def change_func(self, name):
        self.function = name

    # @pyqtSlot(list)
    # def collect_data(self, data=None):
    #     print(data)
    #     if data is None:
    #         data = ['-1', '-1', '0.5', '100']
    #
    #     delay = self.delay_alg()
    #
    #     x = data[0]
    #     y = data[1]
    #     tk = data[2]  # Начальный шаг
    #     M = data[3]  # Количество итераций
    #     alg_name = self.choose_algorithm.currentText()  # Название текущего алгоритма
    #
    #     if alg_name == "Градиентный спуск":
    #         # return gradient_descent(function, x, y, tk, M)
    #         return alg_name
    #     elif alg_name == "Квадратичное программирование":
    #         return alg_name
    #     elif alg_name == "Функция Розенброкка":
    #         return alg_name
    #     elif alg_name == "Рой частиц":
    #         return alg_name
    #     elif alg_name == "Пчелиная оптимизация":
    #         return alg_name
    #     elif alg_name == "Искусственная имунная сеть":
    #         return
    #     elif alg_name == "Бактериальная оптимизация":
    #         return
    #     elif alg_name == "Гибридный алгоритм":
    #         return
