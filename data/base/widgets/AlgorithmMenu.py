from PyQt6.QtCore import QProcess, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import (QVBoxLayout, QWidget, QComboBox, QPushButton, QPlainTextEdit, QStackedLayout)

from data.base.layouts import (Artificial_immune_network, Bacterial_optimization, Bee_optimization, Gradient_descent,
                               Hybrid_algorithm, Quadratic_programming, Rosenbrock_function, Swarm_of_particles)
from data.algorithms import (gradient_descent)


class AlgorithmMenu(QVBoxLayout):
    data_changed = pyqtSignal(list)

    def __init__(self, math_layout):
        super(AlgorithmMenu, self).__init__()
        self.math_layout = math_layout

        # ---------------- ComboBox ---------------- #
        algorithms = ["Градиентный спуск", "Квадратичное программирование", "Функция Розенброкка",
                      "Рой частиц", "Пчелиная оптимизация", "Искусственная имунная сеть",
                      "Бактериальная оптимизация", "Гибридный алгоритм"]
        self.choose_algorithm = QComboBox()
        self.choose_algorithm.addItems(algorithms)
        self.choose_algorithm.currentIndexChanged.connect(self.algorithm_changed)

        self.addWidget(self.choose_algorithm)

        # Словарь слоев
        self.layout_dict = {
            "Градиентный спуск": Gradient_descent.Gradient_descent(),
            "Квадратичное программирование": Quadratic_programming.Quadratic_programming(),
            "Функция Розенброкка": Rosenbrock_function.Rosenbrock_function(),
            "Рой частиц": Swarm_of_particles.Swarm_of_particles(),
            "Пчелиная оптимизация": Bee_optimization.Bee_optimization(),
            "Искусственная имунная сеть": Artificial_immune_network.Artificial_immune_network(),
            "Бактериальная оптимизация": Bacterial_optimization.Bacterial_optimization(),
            "Гибридный алгоритм": Hybrid_algorithm.Hybrid_algorithm()
        }

        # ----------------- Labels ----------------- #

        self.stacked_layout = QStackedLayout()

        # QStackedLayout управляет виджетами, а не макетами напрямую;
        for layout in self.layout_dict.values():
            widget = QWidget()
            widget.setLayout(layout)
            self.stacked_layout.addWidget(widget)

        self.addLayout(self.stacked_layout)

        # ---------------- Button ---------------- #
        self.start_button = QPushButton("Выполнить")
        self.start_button.setCheckable(True)
        self.start_button.clicked.connect(self.collect_data)

        self.addWidget(self.start_button)

        # --------------- Console --------------- #
        self.process = None  # Значение текущего процесса

        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)

        self.addWidget(self.console)

    # Функция обрабатывающая выбор алгоритмов
    def algorithm_changed(self, index):  # i is an int
        print('changed to ' + str(index))
        algorithm_name = self.choose_algorithm.itemText(index)
        layout = self.layout_dict.get(algorithm_name)

        # Получим индекс виджета, который содержит необходимый layout (макет)
        if layout:
            index_widget = self.stacked_layout.indexOf(layout.parentWidget())
            self.stacked_layout.setCurrentIndex(index_widget)
        else:
            print("Реализация алгоритма не найдена!")
        # if index == 0:

    # Консольные функции
    def message(self, s):
        self.console.appendPlainText(s)

    def start_process(self):
        if self.process is None:  # Если текущего процесса нет.
            self.message("Executing process")
            self.process = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.
            self.process.finished.connect(self.process_finished)  # Очистка процесса.
            self.process.start("python3", ['gradient_descent.py'])

    def process_finished(self):
        self.message("Process finished.")
        self.process = None

    @pyqtSlot(float, float, float, float, float)
    def collect_data(self, x=None, y=None, step=None, iterations=None, delay=None):
        index = self.stacked_layout.currentIndex()

        layouts = {
            0: Gradient_descent.Gradient_descent,
            1: Quadratic_programming.Quadratic_programming,
            2: Rosenbrock_function.Rosenbrock_function,
            3: Swarm_of_particles.Swarm_of_particles,
            4: Bee_optimization.Bee_optimization,
            5: Artificial_immune_network.Artificial_immune_network,
            6: Bacterial_optimization.Bacterial_optimization,
            7: Hybrid_algorithm.Hybrid_algorithm
        }
        layout_functions = {
            0: gradient_descent.gradient_descent
            # 1: quadratic_programming.quadratic_programming,
            # 2: rosenbrock_function.rosenbrock_function,
            # 3: swarm_of_particles.swarm_of_particles,
            # 4: bee_optimization.bee_optimization,
            # 5: artificial_immune_network.artificial_immune_network,
            # 6: bacterial_optimization.bacterial_optimization,
            # 7: hybrid_algorithm.hybrid_algorithm
        }

        selected_layout = layouts.get(index)
        selected_function = layout_functions.get(index)

        if selected_function:
            best = selected_function(x, y, step, iterations, delay)
            print(best)
            # self.data_changed.emit(best)
        else:
            print("необходимый layout не найден!")

    # def run_optimization(self):
    #     # Получите выбранный алгоритм и функцию
    #     selected_algorithm = self.choose_algorithm.currentText()
    #     selected_function = self.layout_dict[selected_algorithm]
    #
    #     # Здесь вы должны получить начальные значения x0 и y0, шаг tk, M и другие параметры ввода,
    #     # которые могут понадобиться для градиентного спуска.
    #
    #     x0, y0 = 3, 3 # начальные значения
    #     tk = 0 # шаг
    #     M =  # M
    #     # Определите параметры e1, e2, которые используются в градиентном спуске.
    #
    #     # Запустите градиентный спуск
    #     for x, y, k, f in gradient_descent(selected_function, x0, y0, tk, M):
    #         # Обновите график в MathLayout
    #         self.math_layout.plot_points([x], [y], [f])
    #         # Выведите информацию о текущем шаге в консоль
    #         self.message(f'Step {k}: x={x}, y={y}, f={f}')
    #
    #     # Оповестите о завершении процесса
    #     self.message("Optimization finished.")
