import numpy.linalg as la


def newton(function, d_function, dd_function, initial_guesses):

    for i in range(1,10000):
        x = initial_guesses[-1]
        s = la.solve(dd_function(x), d_function(x))
        next_guess = x - s
        print(function(next_guess), next_guess)

        initial_guesses.append(next_guess)

