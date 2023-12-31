from PyQt6.QtCore import pyqtSlot, QTimer
from PyQt6.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from data.functions import (holder_table_function, himmelblau, sphere_function, mathias_function, izoma_function,
                            ackley_function, rozenbroke)


class MplCanvas(FigureCanvas):
    def __init__(self):
        fig = Figure(figsize=(15, 6))
        self.ax = fig.add_subplot(111, projection='3d')
        super(MplCanvas, self).__init__(fig)

        self.mpl_connect('button_press_event', self.ax._button_press)
        self.mpl_connect('button_release_event', self.ax._button_release)
        self.mpl_connect('motion_notify_event', self.ax._on_move)
        # self.mpl_connect('scroll_event', self.on_scroll)

        self.pressed = False
        self.lastx = None
        self.lasty = None


class MathLayout(QVBoxLayout):

    def __init__(self):
        super().__init__()

        # Создание сетки и задание основы графика
        self.canvas = MplCanvas()
        self.addWidget(self.canvas)
        # self.bar = None

        # Инициализация таймера для обновления графика
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.interval = 3000  # Интервал времени в миллисекундах (здесь 1 секунда)

    # Отрисовка графиков их FunctionMenu
    @pyqtSlot(list, list, str, int)
    def update_canvas(self, x_intervals=None, y_intervals=None, scale=None, selected_function=None):
        self.clear_plot()
        if selected_function == 0:
            X, Y, Z = himmelblau(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet', alpha=0.5)
            print('himmelblau')
        elif selected_function == 1:
            X, Y, Z = sphere_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet', alpha=0.5)
            print('sphere_function')
        elif selected_function == 2:
            X, Y, Z = mathias_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet', alpha=0.5)
            print('mathias_function')
            self.canvas.draw()
        elif selected_function == 3:
            X, Y, Z = izoma_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet', alpha=0.5)
            print('izoma_function')
            self.canvas.draw()
        elif selected_function == 4:
            X, Y, Z = ackley_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z-1, cmap='jet', alpha=0.5)
            print('ackley_function')
            self.canvas.draw()
        elif selected_function == 5:
            X, Y, Z = holder_table_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z - 1, cmap='jet', alpha=0.5)
            print('holder_table_function')
            self.canvas.draw()
        elif selected_function == 6:
            X, Y, Z = rozenbroke(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z - 1, cmap='jet', alpha=0.5)
            print('rozenbroke')
            self.canvas.draw()
        else:
            print('Выход за предел выбора функции')

    def start_timer(self):
        self.timer.start(self.interval)

    def stop_timer(self):
        self.timer.stop()

    @pyqtSlot(list, float, object, object)
    def plot_points(self, result, delay, message, stop):
        self.points_to_plot = result
        self.index = 0
        self.interval = int(delay)
        self.console = message
        self.stop = stop

        self.start_timer()

    def update_plot(self):
        if self.index < len(self.points_to_plot):
            x, y, z = self.points_to_plot[self.index]
            self.console(f'{round(x, 4),round(y,4),round(z,4)}')
            self.canvas.ax.scatter(x, y, z, c='r', marker='o')
            self.canvas.draw()
            self.index += 1
        else:
            self.console("Конец выполнения.")
            self.stop_timer()

    def clear_plot(self):
        self.canvas.ax.clear()
