import numpy.linalg as la
from scipy import optimize
import time


def newton(fun, initial_guesses, steps):
    start_time = time.time()
    i = 0
    fprime = lambda x: optimize.approx_fprime(x, fun, 0.0001)
    fprime2 = lambda x: optimize.approx_fprime(x, fprime, 0.0001)
    while i <steps:
        x = initial_guesses[-1]
        s = la.solve(fprime2(x), fprime(x))
        next_guess = x - s
        initial_guesses.append(next_guess)
        i = i +1
    return (initial_guesses[-1], fun(initial_guesses[-1]), time.time() - start_time)



