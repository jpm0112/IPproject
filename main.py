
from scipy import optimize
from problems import *
from functions import *
import numpy as np
import time

start_time = time.time()
fun = evaluate_ackley
initial_guesses = [np.array([0.00011, 0.0111])]
fprime = lambda x: optimize.approx_fprime(x, fun, 0.0001)
fprime2 = lambda x: optimize.approx_fprime(x, fprime, 0.0001)
solution = newton(fun, fprime, fprime2, initial_guesses, 200)
solution
elapsed_time = time.time() - start_time


start_time = time.time()
fun = evaluate_bona
initial_guesses = [np.array([0.00011, 0.0111])]
fprime = lambda x: optimize.approx_fprime(x, fun, 0.0001)
fprime2 = lambda x: optimize.approx_fprime(x, fprime, 0.0001)
solution = newton(fun, fprime, fprime2, initial_guesses, 200)
solution
elapsed_time = time.time() - start_time


start_time = time.time()
fun = evaluate_threecamel
initial_guesses = [np.array([0.00011, 0.0111])]
fprime = lambda x: optimize.approx_fprime(x, fun, 0.0001)
fprime2 = lambda x: optimize.approx_fprime(x, fprime, 0.0001)
solution = newton(fun, fprime, fprime2, initial_guesses, 200)
solution
elapsed_time = time.time() - start_time












