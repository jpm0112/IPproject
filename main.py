
from scipy import optimize
from problems import *
import numpy as np


initial_guess = [np.array([2, 2./5])]

sol = newton()

fprime = lambda x: optimize.approx_fprime(x, evaluate_ackley, 0.01)
root = optimize.minimize(evaluate_ackley, initial_guess, method="Newton-CG", jac = fprime)
root

res = optimize.minimize(evaluate_ackley, initial_guess, method='Nelder-Mead', tol=1e-6)


evaluate_ackley(0,1)
initial_guess[1]






