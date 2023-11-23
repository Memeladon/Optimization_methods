import numpy as np


def f(xgrid, ygrid):
    return 2 * np.power(xgrid, 2) + 3 * np.power(ygrid, 2) + (4 * xgrid * ygrid) - (6 * xgrid) - (3 * ygrid)
    # return xgrid ** 2 + ygrid ** 2


def get_index(func, elem):
    for i in range(len(func)):
        if func[i] == elem:
            return i
    return 0


def simplex_method(x1, x2):
    triangle = []
    x0 = float(x1)
    z0 = float(x2)
    e = 5
    alpha = 2
    points = [[x0 - alpha / 2, z0 - 0.29 * alpha],
              [x0 + alpha / 2, z0 - 0.29 * alpha],
              [x0, z0 + 0.58 * alpha]]
    func = [f(points[0][0], points[0][1]),
            f(points[1][0], points[1][1]),
            f(points[2][0], points[2][1])]
    triangle.append(list(points))
    x_min = x0
    z_min = z0
    y_min = f(x0, z0)
    flag = 0
    x_max = x0
    z_max = z0
    while abs(f(x_max, z_max) - min(func)) > e:
        if flag:
            flag = 0
            x0, z0 = points[get_index(func, min(func))]
            x0 += points[get_index(func, max(func))][0]
            z0 += points[get_index(func, max(func))][1]
            x0 /= 2
            z0 /= 2
            points.remove(points[get_index(func, max(func))])
            func.remove(max(func))
            x1, z1 = points[get_index(func, min(func))]
            x1 += points[get_index(func, max(func))][0]
            z1 += points[get_index(func, max(func))][1]
            x1 /= 2
            z1 /= 2
            points.remove(points[get_index(func, max(func))])
            func.remove(max(func))
            func.append(f(x0, z0))
            points.append([x0, z0])
            func.append(f(x1, z1))
            points.append([x1, z1])
        else:
            x_max, z_max = points[get_index(func, max(func))]
            points.remove(points[get_index(func, max(func))])
            func.remove(max(func))
            x0 = 0 - x_max
            z0 = 0 - z_max
            for value in points:
                x0 += value[0]
                z0 += value[1]
            if f(x0, z0) > max(func):
                func.append(f(x_max, z_max))
                points.append([x_max, z_max])
                flag = 1
            else:
                func.append(f(x0, z0))
                points.append([x0, z0])

        if f(x_min, z_min) > min(func):
            x_min, z_min = points[get_index(func, min(func))]
            y_min = min(func)

        triangle.append(list(points))

    x_min = round(x_min, 2)
    z_min = round(z_min, 2)
    y_min = round(y_min, 2)
    return triangle, x_min, y_min, z_min


def get_points(start_x, start_y):
    triangle, x_min, z_min, y_min = simplex_method(start_x, start_y)
    points = []
    for tr in triangle:
        if min(tr)[1] > y_min:
            point = [tr[0][0], tr[0][1], min(tr)[1]]
            points.append(point)
        else:
            points.append([x_min, y_min, z_min])
            break
    return points


# points = get_points(10, 2)
# print(points)
