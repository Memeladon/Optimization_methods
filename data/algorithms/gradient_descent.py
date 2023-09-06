import numpy as np
import numdifftools as nd


def partial_function(f___, input, pos, value):
    tmp = input[pos]
    input[pos] = value
    ret = f___(*input)
    input[pos] = tmp
    return ret


def gradient(function, input):
    """Частная произвоздная по каждому из параметров функции f(т.е. градиент)"""

    ret = np.empty(len(input))
    for i in range(len(input)):
        fg = lambda x: partial_function(function, input, i, x)
        ret[i] = nd.Derivative(fg)(input[i])
    return ret


def next_point(x, y, gx, gy, step) -> tuple:
    return x - step * gx, y - step * gy


def gradient_descent(function, x0, y0, tk, M):
    yield x0, y0, 0, function(x0, y0)

    e1 = 0.0001
    e2 = 0.0001

    k = 0
    while True:
        (gx, gy) = gradient(function, [x0, y0])  # 3

        if np.linalg.norm((gx, gy)) < e1:  # Шаг 4. Проверить выполнение критерия окончания
            break

        if k >= M:  # Шаг 5
            break

        x1, y1 = next_point(x0, y0, gx, gy, tk)  # 7
        f1 = function(x1, y1)
        f0 = function(x0, y0)
        while not f1 < f0:  # 8 условие
            tk = tk / 2
            x1, y1 = next_point(x0, y0, gx, gy, tk)
            f1 = function(x1, y1)
            f0 = function(x0, y0)

        if np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2) < e2 and abs(f1 - f0) < e2:  # 9
            x0, y0 = x1, y1
            break
        else:
            k += 1
            x0, y0 = x1, y1
            yield x0, y0, k, f1
