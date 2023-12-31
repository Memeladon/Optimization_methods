import re

from PyQt6.QtCore import QProcess, pyqtSignal, pyqtSlot, Qt
from PyQt6.QtWidgets import (QVBoxLayout, QComboBox, QPushButton, QPlainTextEdit, QLabel,
                             QLineEdit, QGridLayout)

from data.algorithms import (gradient_descent, get_points, Swarm, genetic_algorithm, algorithm_of_bees,
                             algorithm_artificial_immune_system, algorithm_is_bacterial)
from data.algorithms.hybrid_optimization_algorithm.hybrid import gibrid
from data.functions import (HolderTableFunction, Himmelblau, SphereFunction, MathiasFunction, IzomaFunction,
                            AckleyFunction, Rozenbroke)


class AlgorithmMenu(QVBoxLayout):
    data_changed = pyqtSignal(list)
    points = pyqtSignal(list, float, object, object)
    function = 'Функция Химмельблау'

    def __init__(self, math_layout):
        super(AlgorithmMenu, self).__init__()
        self.math_layout = math_layout

        # ---------------- ComboBox ---------------- #
        algorithms = ["Градиентный спуск", "Квадратичное программирование", "Генетический алгоритм",
                      "Рой частиц", "Пчелиная оптимизация", "Искусственная имунная сеть",
                      "Бактериальная оптимизация", "Гибридный алгоритм"]
        self.choose_algorithm = QComboBox()
        self.choose_algorithm.addItems(algorithms)
        self.choose_algorithm.currentIndexChanged.connect(self.algorithm_changed)
        self.addWidget(self.choose_algorithm)

        self.functions_dict = {
            "Функция Химмельблау": Himmelblau.objective,
            "Функция сферы": SphereFunction.objective,
            "Функция Матьяса": MathiasFunction.objective,
            "Функция Изома": IzomaFunction.objective,
            "Функция Экли": AckleyFunction.objective,
            "Табличная функция Хольдера": HolderTableFunction.objective,
            "Функция Розенброка": Rozenbroke.objective
        }

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

        # ЗАДЕРЖКА ВЫВОДА ТОЧЕК
        self.label_delay = QLabel('&Задержка')
        self.label_delay.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_delay = QLineEdit('1')
        self.lineEdit_delay.textChanged[str].connect(self.delay_alg)
        self.label_delay.setBuddy(self.lineEdit_delay)

        # РАЗМЕР ПОПУЛЯЦИЙ
        self.label_population_size = QLabel('&Размер популяций')
        self.label_population_size.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_population_size = QLineEdit('50')
        self.lineEdit_population_size.textChanged[str].connect(self.population_size_alg)
        self.label_population_size.setBuddy(self.lineEdit_population_size)

        self.label_population_size.setDisabled(True)
        self.lineEdit_population_size.setDisabled(True)

        # КОЛИЧЕСТВО ПОКОЛЕНИЙ
        self.label_num_generations = QLabel('&Количество поколений')
        self.label_num_generations.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lineEdit_num_generations = QLineEdit('100')
        self.lineEdit_num_generations.textChanged[str].connect(self.num_generations_alg)
        self.label_num_generations.setBuddy(self.lineEdit_num_generations)

        self.label_num_generations.setDisabled(True)
        self.lineEdit_num_generations.setDisabled(True)

        # ----------------- grid ----------------- #
        grid_layout.addWidget(self.label_x, 0, 0)
        grid_layout.addWidget(self.lineEditX, 0, 1)

        grid_layout.addWidget(self.label_y, 1, 0)
        grid_layout.addWidget(self.lineEditY, 1, 1)

        grid_layout.addWidget(self.label_first_step, 2, 0)
        grid_layout.addWidget(self.lineEdit_first_step, 2, 1)

        grid_layout.addWidget(self.label_iterations, 3, 0)
        grid_layout.addWidget(self.lineEdit_iterations, 3, 1)

        grid_layout.addWidget(self.label_delay, 4, 0)
        grid_layout.addWidget(self.lineEdit_delay, 4, 1)

        grid_layout.addWidget(self.label_population_size, 5, 0)
        grid_layout.addWidget(self.lineEdit_population_size, 5, 1)

        grid_layout.addWidget(self.label_num_generations, 6, 0)
        grid_layout.addWidget(self.lineEdit_num_generations, 6, 1)

        self.addLayout(grid_layout)

        # ---------------- Button ---------------- #
        self.start_button = QPushButton("Выполнить")
        self.start_button.clicked.connect(self.start_process)
        self.addWidget(self.start_button)

        self.stop_button = QPushButton("Остановить")
        self.stop_button.clicked.connect(self.stop_process)  # Corrected this line
        self.addWidget(self.stop_button)

        # --------------- Console --------------- #
        self.process = None  # Значение текущего процесса
        self.console = QPlainTextEdit()
        self.console.setReadOnly(True)
        self.addWidget(self.console)

    def algorithm_changed(self, index):
        print(index)
        if index == 4 or index == 6:
            self.label_num_generations.setDisabled(True)
            self.lineEdit_num_generations.setDisabled(True)

            self.label_population_size.setDisabled(False)
            self.lineEdit_population_size.setDisabled(False)
            self.lineEdit_population_size.setText('100')
        elif index == 5:
            self.label_num_generations.setDisabled(False)
            self.lineEdit_num_generations.setDisabled(False)
            self.lineEdit_num_generations.setText('200')

            self.label_population_size.setDisabled(False)
            self.lineEdit_population_size.setDisabled(False)
            self.lineEdit_population_size.setText('100')
        elif index == 7:
            self.label_num_generations.setDisabled(False)
            self.lineEdit_num_generations.setDisabled(False)
            self.lineEdit_num_generations.setText('100')

            self.label_population_size.setDisabled(False)
            self.lineEdit_population_size.setDisabled(False)
            self.lineEdit_population_size.setText('100')
        elif index > 1:
            self.label_num_generations.setDisabled(False)
            self.lineEdit_num_generations.setDisabled(False)
            self.lineEdit_num_generations.setText('650')

            self.label_population_size.setDisabled(False)
            self.lineEdit_population_size.setDisabled(False)
            self.lineEdit_population_size.setText('100')
        else:
            self.label_num_generations.setDisabled(True)
            self.lineEdit_num_generations.setDisabled(True)

            self.label_population_size.setDisabled(True)
            self.lineEdit_population_size.setDisabled(True)

    # Функция обрабатывающая изменения в строке алгоритмов (Delay)
    def delay_alg(self):
        input_text = self.lineEdit_delay.text()
        clear = self.process_input_text(input_text)
        # Тут еще дописать обработку надо (или переделать 'process_input_text')
        if clear[0] == '0':
            clear = clear[:1] + '.' + clear[1:]
        print('Задержка: ' + str(clear))
        return float(clear)

    # Функция обрабатывающая изменения в строке алгоритмов (X)
    def x_alg(self):
        input_text = self.lineEditX.text()
        clear = self.process_input_text(input_text)
        print('X: ' + str(clear))
        return float(clear)

    # Функция обрабатывающая изменения в строке алгоритмов (Y)
    def y_alg(self):
        input_text = self.lineEditY.text()
        clear = self.process_input_text(input_text)
        print('Y: ' + str(clear))
        return float(clear)

    # Функция обрабатывающая изменения в строке алгоритмов (Steps)
    def step_alg(self):
        input_text = self.lineEdit_first_step.text()
        clear = self.process_input_text(input_text).replace('-', '')
        # Тут еще дописать обработку надо (или переделать 'process_input_text')
        if clear[0] == '0':
            clear = clear[:1] + '.' + clear[1:]
        print('Начальный шаг: ' + str(clear))
        return float(clear)

    # Функция обрабатывающая изменения в строке алгоритмов (Iterations)
    def iter_alg(self):
        input_text = self.lineEdit_iterations.text()
        clear = self.process_input_text(input_text).replace('-', '')
        print('Число итераций: ' + str(clear))
        return int(clear)

    # Функция обрабатывающая изменения в строке размерности популяции (Population_size)
    def population_size_alg(self):
        input_text = self.lineEdit_population_size.text()
        clear = self.process_input_text(input_text).replace('-', '')
        print('Размерность популяции: ' + str(clear))

        return int(clear)

    # Функция обрабатывающая изменения в строке количества поколений (Num_generations)
    def num_generations_alg(self):
        input_text = self.lineEdit_num_generations.text()
        clear = self.process_input_text(input_text).replace('-', '')
        print('Количества поколений: ' + str(clear))

        return int(clear)

    def process_input_text(self, input_text):
        # Очистка текста от недопустимых символов с помощью регулярного выражения
        clear_text = re.sub(r'[^\d-]', '', input_text)

        # Удаление лишних знаков минус и точек

        clear_text = re.sub(r'(?!^\d)|\.(?=(.*\.)+)', '', clear_text)

        if clear_text == '' or clear_text == '-':
            return '0'

        # Первый символ должен быть цифрой или минусом
        if clear_text and not clear_text[0].isdigit() and clear_text[0] != '-':
            clear_text = clear_text[1:]

        return clear_text

    # Консольные функции
    def message(self, s):
        self.console.appendPlainText(s)

    def start_process(self):
        if self.process is None:  # Если текущего процесса нет.
            # data = self.collect_data()

            delay = int(self.delay_alg() * 1000)
            x = self.x_alg()
            y = self.y_alg()
            tk = self.step_alg()  # Начальный шаг
            M = self.iter_alg()  # Количество итераций
            population_size = self.population_size_alg()
            num_generations = self.num_generations_alg()
            alg_name = self.choose_algorithm.currentText()  # Название текущего алгоритма

            self.message(f"Выполнение алготима: {alg_name}.")
            self.process = QProcess()  # Keep a reference to the QProcess (e.g. on self) while it's running.

            if alg_name == "Градиентный спуск":
                result = gradient_descent(self.functions_dict[self.function], x, y, tk, M)

            elif alg_name == "Квадратичное программирование":
                result = get_points(x, y)

            elif alg_name == "Генетический алгоритм":
                # Запуск генетического алгоритма
                best_solution, best_fitness, arr_points = genetic_algorithm(self.functions_dict[self.function],
                                                                            population_size, num_generations)
                result = arr_points

            elif alg_name == "Рой частиц":
                a = Swarm(population_size, 0.1, 1, 5, num_generations,
                          self.functions_dict[self.function], -5, 5)
                result = a.startSwarm()

            elif alg_name == "Пчелиная оптимизация":
                result, bestPoints = algorithm_of_bees(-10, 10, -10, 10, population_size,
                                                       self.functions_dict[self.function], 200)

            elif alg_name == "Искусственная имунная сеть":
                best_point, result = algorithm_artificial_immune_system(-10, 10, -10, 10, population_size,
                                                                        self.functions_dict[self.function],
                                                                        num_generations)
            elif alg_name == "Бактериальная оптимизация":
                history, bestPoint = algorithm_is_bacterial(-10, 10, -10, 5, population_size,
                                                            self.functions_dict[self.function], 200, 0.1)
                result = []
                for item in history:
                    result += item[0], item[1], item[2]

            elif alg_name == "Гибридный алгоритм":
                points, bestPoint = gibrid(population_size, num_generations, self.functions_dict[self.function])

                result = []
                for item in points:
                    result += item[0], item[1], item[2]

            self.message('x, y, z')
            self.points.emit(result, delay, self.message, self.stop_process)
            self.process.finished.connect(self.process_finished)  # Очистка процесса.
            self.process_finished()

    def process_finished(self):
        self.process = None

    def stop_process(self):
        if self.process is not None and self.process.state() == QProcess.Running:
            self.process.kill()
            self.message("Процесс остановлен.")
            print('Stopped')
            return False

    @pyqtSlot(str)
    def change_func(self, name):
        self.function = name
