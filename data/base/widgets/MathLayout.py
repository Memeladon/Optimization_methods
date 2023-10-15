from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from data.Functions.Himmelblau import himmelblau
from data.Functions.UnimodalFunction1 import unimodal_one


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
        self.canvas.ax.clear()

        if selected_function == 0:
            X, Y, Z = himmelblau(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet')
        elif selected_function == 1:
            X, Y, Z = unimodal_one(x_intervals, y_intervals, scale)
            self.canvas.ax.plot_surface(X, Y, Z, cmap='jet')

        self.canvas.draw()
