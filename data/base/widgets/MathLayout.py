import numpy as np
from PyQt6.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from data.Functions.Himmelblau import himmelblau


class MathLayout(QVBoxLayout):
    def __init__(self, interval_x, interval_y, z_scale):
        super().__init__()

        # Создание сетки и задание основы графика
        self.fig = Figure(figsize=(15, 6))
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.canvas.mpl_connect('button_press_event', self.ax._button_press)
        self.canvas.mpl_connect('button_release_event', self.ax._button_release)
        self.canvas.mpl_connect('motion_notify_event', self.ax._on_move)

        self.addWidget(self.canvas)

        self.interv_x = interval_x
        self.interv_y = interval_y
        self.scale_z = z_scale
        self.bar = None

        # Выбор/задание функции
        X, Y, Z = himmelblau(self.interv_x, self.interv_y, self.scale_z)

        # Отрисовка
        self.ax.plot_surface(X, Y, Z, cmap='jet')

    # def update_canvas(self):
    #     x_position = [0.5]
    #
    #     if self.bar:
    #         self.bar.remove()
    #     self.bar = self.ax.bar(x_position, value, width=0.2, color='g')
    #     self.canvas.draw()
