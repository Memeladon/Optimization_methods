from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class MathLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        # Создание сетки и задание основы графика
        fig = Figure()
        canvas = FigureCanvas(fig)
        axes = fig.add_subplot(111, projection='3d')

        self.addWidget(canvas)

        # Выбор/задание функции
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        R = np.sqrt(X ** 2 + Y ** 2)
        Z = np.sin(R)

        # Отрисовка
        axes.plot_surface(X, Y, Z)



