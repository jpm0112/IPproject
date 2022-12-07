
from scipy import optimize
from problems import *
from functions import *
import numpy as np


fun = evaluate_ackley
initial_guesses = [np.array([0.00011, 0.0111])]
fprime = lambda x: optimize.approx_fprime(x, fun, 0.0001)
fprime2 = lambda x: optimize.approx_fprime(x, fprime, 0.0001)

solution = newton(fun, fprime, fprime2, initial_guesses, 200)
solution


fun = evaluate_bona
initial_guesses = [np.array([0.00011, 0.0111])]
fprime = lambda x: optimize.approx_fprime(x, fun, 0.0001)
fprime2 = lambda x: optimize.approx_fprime(x, fprime, 0.0001)

solution = newton(fun, fprime, fprime2, initial_guesses, 200)
solution


fun = evaluate_threecamel
initial_guesses = [np.array([0.00011, 0.0111])]
fprime = lambda x: optimize.approx_fprime(x, fun, 0.0001)
fprime2 = lambda x: optimize.approx_fprime(x, fprime, 0.0001)

solution = newton(fun, fprime, fprime2, initial_guesses, 200)
solution
























root = optimize.minimize(evaluate_ackley, initial_guesses, method="Newton-CG", jac = fprime)
res = optimize.minimize(evaluate_ackley, initial_guesses, method='Nelder-Mead', tol=1e-6)








