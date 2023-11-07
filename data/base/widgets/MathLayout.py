from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from data.functions import (holder_table_function, himmelblau, sphere_function, mathias_function, izoma_function,
                            ackley_function)


class MplCanvas(FigureCanvas):
    def __init__(self):
        fig = Figure(figsize=(15, 6))
        self.ax = fig.add_subplot(111, projection='3d')
        super(MplCanvas, self).__init__(fig)

        self.mpl_connect('button_press_event', self.ax._button_press)
        self.mpl_connect('button_release_event', self.ax._button_release)
        self.mpl_connect('motion_notify_event', self.ax._on_move)


class MathLayout(QVBoxLayout):

    def __init__(self):
        super().__init__()

        # Создание сетки и задание основы графика
        self.canvas = MplCanvas()
        self.addWidget(self.canvas)
        # self.bar = None

    # Отрисовка графиков их FunctionMenu
    @pyqtSlot(list, list, str, int)
    def update_canvas(self, x_intervals=None, y_intervals=None, scale=None, selected_function=None):
        self.clear_plot()
        if selected_function == 0:
            X, Y, Z = himmelblau(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet')
            print('himmelblau')
        elif selected_function == 1:
            X, Y, Z = sphere_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet')
            print('sphere_function')
        elif selected_function == 2:
            X, Y, Z = mathias_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet')
            print('mathias_function')
            self.canvas.draw()
        elif selected_function == 3:
            X, Y, Z = izoma_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet')
            print('izoma_function')
            self.canvas.draw()
        elif selected_function == 4:
            X, Y, Z = ackley_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet')
            print('ackley_function')
            self.canvas.draw()
        elif selected_function == 5:
            X, Y, Z = holder_table_function(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet')
            print('holder_table_function')
            self.canvas.draw()
        else:
            print('Выход за предел выбора функции')

    # @pyqtSlot(list)
    # def algorithms_execution(self, x, y, step, iterations, delay, selected_algorithm):

    def plot_points(self, x, y, z, color='r', marker='o'):
        self.canvas.ax.scatter(x, y, z, c=color, marker=marker)
        self.canvas.draw()

    def clear_plot(self):
        self.canvas.ax.clear()
