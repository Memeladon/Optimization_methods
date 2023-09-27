import numpy as np
from PyQt6.QtWidgets import QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from data.Functions.Himmelblau import himmelblau


class MathLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        # Создание сетки и задание основы графика
        fig = Figure()
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111, projection='3d')

        canvas.mpl_connect('button_press_event', ax._button_press)
        canvas.mpl_connect('button_release_event', ax._button_release)
        canvas.mpl_connect('motion_notify_event', ax._on_move)

        self.addWidget(canvas)

        # Выбор/задание функции
        X, Y, Z = himmelblau()

        # Отрисовка
        ax.plot_surface(X, Y, Z, cmap='jet')
