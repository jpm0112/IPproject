

from problems import *
from functions import *
import numpy as np


initial_guesses = [np.array([3, 0.03])]

fun = evaluate_ackley
res = newton(fun, initial_guesses, 200)
res[3]

fun = evaluate_bona
res = newton(fun, initial_guesses, 200)
res


fun = evaluate_threecamel
res = newton(fun, initial_guesses, 200)
res[3]


res[0]


import matplotlib.pyplot as plt
xmesh, ymesh = np.mgrid[1:5:50j,-2:1:50j]
fmesh = fun(np.array([xmesh, ymesh]))
guesses = res[3]
plt.axis("equal")
plt.contour(xmesh, ymesh, fmesh, 50)
it_array = np.array(guesses)
plt.plot(it_array.T[0], it_array.T[1], "x-")
plt.show()












