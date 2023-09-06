# Файл, который запустит наше окно
# import PyQt
# import OpenGL

class View:
    def __new__(cls, *args, **kwargs):
        print("Create instance")
        return super().__new__(cls)

    def __init__(self, height, width):
        window_hight = height
        window_width = width
        Output_interval = 0.1

    def render(self):
        # Вывод окна
        None
