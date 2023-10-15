# unimodal test function
from numpy import arange
from numpy import meshgrid


# objective function
def objective(x, y):
    return x ** 2.0 + y ** 2.0


def unimodal_one(x_intrvs, y_intervs, z_scale):
    # define range for input
    r_min_x, r_max_x = float(x_intrvs[0]), float(y_intervs[1])
    r_min_y, r_max_y = float(y_intervs[0]), float(y_intervs[1])
    z = float(z_scale)
    # sample input range uniformly at 0.1 increments
    xaxis = arange(r_min_x, r_max_x, 0.1)
    yaxis = arange(r_min_y, r_max_y, 0.1)
    # create a mesh from the axis
    x, y = meshgrid(xaxis, yaxis)
    # compute targets
    results = objective(x, y)

    return x, y, results + z
