# multimodal test function
from matplotlib import pyplot
from numpy import arange
from numpy import meshgrid


# objective function
def objective(x, y):
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2


def himmelblau():
    # define range for input
    r_min, r_max = -5.0, 5.0
    # sample input range uniformly at 0.1 increments
    xaxis = arange(r_min, r_max, 0.1)
    yaxis = arange(r_min, r_max, 0.1)
    # create a mesh from the axis
    x, y = meshgrid(xaxis, yaxis)
    # compute targets
    results = objective(x, y)

    return x, y, results

