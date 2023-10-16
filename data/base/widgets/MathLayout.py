from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from data.functions.Himmelblau import himmelblau
from data.functions.SphereFunction import sphere_function


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
        # best_x, best_y, best_value = next(best_results)
        # self.plot_best_point(best_x, best_y)
        self.canvas.draw()

    # def plot_best_point(self, x, y):
    #     self.canvas.ax.plot([x], [y], [function(x, y)], 'ro')  # 'ro' - красные точки
    #     self.canvas.draw()

    def clear_plot(self):
        self.canvas.ax.clear()
