
from scipy import optimize
from problems import *
from functions import *
import numpy as np



fun = evaluate_ackley
initial_guesses = [np.array([0.00011, 0.0111])]
res = newton(fun, initial_guesses, 200)


fun = evaluate_bona
initial_guesses = [np.array([0.00011, 0.0111])]
res = newton(fun, initial_guesses, 200)
res


fun = evaluate_threecamel
initial_guesses = [np.array([0.00011, 0.0111])]
res = newton(fun, initial_guesses, 200)
res















