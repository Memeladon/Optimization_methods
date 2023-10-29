# multimodal test function
from numpy import arange
from numpy import cos
from numpy import e
from numpy import exp
from numpy import meshgrid
from numpy import pi
from numpy import sqrt


# objective function
def objective(x, y):
	return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20


def ackley_function(x_intrvs, y_intervs, z_scale):
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
