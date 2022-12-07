import numpy.linalg as la
import numpy as np


def newton(function, fprime, fprime2, initial_guesses, steps):
    i = 0
    while i <steps:
        x = initial_guesses[-1]
        s = la.solve(fprime2(x), fprime(x))
        next_guess = x - s
        initial_guesses.append(next_guess)
        i = i +1
    return (function(initial_guesses[-1]))



