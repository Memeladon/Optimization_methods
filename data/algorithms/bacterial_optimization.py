import random
import copy


# класс - Бактерия
class Bacteria:
    def __init__(self, min_x, max_x, min_y, max_y, function):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.function = function
        self.arr_move = []
        self.arr_fitness = []
        # вектор V
        self.Vx = random.uniform(-1, 1)
        self.Vy = random.uniform(-1, 1)
        self.initialize()

    def initialize(self):
        rand_x = round(random.uniform(self.min_x, self.max_x), 5)
        rand_y = round(random.uniform(self.min_y, self.max_y), 5)
        z = round(self.function(rand_x, rand_y), 5)
        self.arr_move.append((rand_x, rand_y))
        self.arr_fitness.append(z)

    def health(self):
        return sum(self.arr_fitness)

    def getMove(self):
        return self.arr_move

    def takingStep(self, new_x, new_y):
        z = round(self.function(new_x, new_y), 5)
        self.arr_move.append((new_x, new_y))
        self.arr_fitness.append(z)

    # Получим личный индекс V для данной бактерии
    def getV(self):
        return self.Vx, self.Vy

    # Меняем значение вектора V для какждого при скачке бактерии
    def reV(self):
        self.Vx = random.uniform(-1, 1)
        self.Vy = random.uniform(-1, 1)


# ммеханизм хемотаксиса
def chemotaxis(bacteria, l, func):
    moveList = bacteria.getMove()
    lastPoitn = moveList[len(moveList) - 1]
    new_x = lastPoitn[0] + l * (bacteria.Vx / abs(bacteria.Vx))
    new_y = lastPoitn[1] + l * (bacteria.Vy / abs(bacteria.Vy))

    if func(lastPoitn[0], lastPoitn[1]) < func(new_x, new_y):
        bacteria.reV()
        bacteria.takingStep(lastPoitn[0], lastPoitn[1])
    else:
        bacteria.takingStep(new_x, new_y)
    return bacteria


# Реализация репродукции
def reproduction(colonyBacteria):
    newColonyBacteria = []
    lenth = len(colonyBacteria) // 2
    for i in range(lenth):
        newColonyBacteria.append(colonyBacteria[i])
        newColonyBacteria.append(copy.deepcopy(colonyBacteria[i]))
    return newColonyBacteria


# Реализация ликвидации и рассеивания
def liquidationAndDispersion(colonyBacteria, e, min_x, max_x, min_y, max_y, function):
    for bacteria in range(len(colonyBacteria)):
        u = random.uniform(0, 1)
        # Если u меньше заданной e, то данную бактерию ликвидируем и на её место
        # ставим новую бактерию с в случаёной точке
        if u < e:
            newBacteria = Bacteria(min_x, max_x, min_y, max_y, function)
            colonyBacteria[bacteria] = newBacteria

    return colonyBacteria


def get_history_best_points(colonyBacteria):
    sortColony = sorted(colonyBacteria, key=lambda x: x.arr_fitness[-1])
    last_points = [bacteria.arr_move[-1] for bacteria in sortColony]
    points = []
    for i in range(len(last_points)):
        points.append([last_points[i][0], last_points[i][1], sortColony[i].arr_fitness[-1]])

    return points


def algorithm_is_bacterial(min_x, max_x, min_y, max_y, number_of_bacteria, function, time, e):
    # колония бактерий
    colonyBacteria = []

    # Зададим параметры
    l = 0.2

    for i in range(number_of_bacteria):
        bacteria = Bacteria(min_x, max_x, min_y, max_y, function)
        colonyBacteria.append(bacteria)
    l = 0.2

    history_best_points = []
    bestPoint = [colonyBacteria[0].arr_move[0][-1], colonyBacteria[0].arr_move[0][-1], colonyBacteria[0].arr_fitness[-1]]

    for i in range(time):
        # Проводим процедуру хемотаксиса
        for bacteria in range(number_of_bacteria):
            if i % 10 == 0:
                l = l / 100 * 90
            colonyBacteria[bacteria] = chemotaxis(colonyBacteria[bacteria], l, function)

        # Сортируем бактерии в порядке уменьшея общего здоровья каждой бактерии
        sortColonyBacteria = sorted(colonyBacteria, key=lambda x: x.health())
        # Этап репродукции
        repColonyBacteria = reproduction(sortColonyBacteria)
        # Реализация ликвидации и рассеивания
        liqColonyBacteria = liquidationAndDispersion(repColonyBacteria, e, min_x, max_x, min_y, max_y, function)

        colonyBacteria = liqColonyBacteria
        # Получение нового массива, состоящего из последней точки каждого объекта

        # Вывод точек на экран
        last_points = get_history_best_points(colonyBacteria)
        history_best_points.append(last_points[0:5])
        if bestPoint[2] > last_points[0][2]:
            bestPoint = last_points[0]
            # print(bestPoint)

    return history_best_points, bestPoint


