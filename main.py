
from scipy import optimize
from problems import *
from functions import *
import numpy as np
import numpy.linalg as la


initial_guesses = [np.array([0.00011, 0.0111])]
fprime = lambda x: optimize.approx_fprime(x, evaluate_ackley, 0.0001)
fprime2 = lambda x: optimize.approx_fprime(x, fprime, 0.0001)

solution = newton(evaluate_ackley, fprime, fprime2, initial_guesses, 200)
solution


i = 0
while i <50:
        x = initial_guesses[-1]
        s = la.solve(fprime2(x), fprime(x))
        print(s)
        next_guess = x - s
        #print(function(next_guess), next_guess)
        initial_guesses.append(next_guess)
        i = i +1
initial_guesses[-1]
evaluate_ackley(initial_guesses[-1])

























root = optimize.minimize(evaluate_ackley, initial_guesses, method="Newton-CG", jac = fprime)
res = optimize.minimize(evaluate_ackley, initial_guesses, method='Nelder-Mead', tol=1e-6)








