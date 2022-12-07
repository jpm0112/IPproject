
import numpy as np

# Ackley function


def evaluate_ackley(list):
    x= list[0]
    y = list[1]
    z1 = -20.0* np.exp(-0.2*np.sqrt(0.5* (x**2 + y**2)))
    z2= - np.exp(0.5* (np.cos(2*np.pi*x) + np.cos(2*np.pi*y)))
    z = z1 + z2 + np.exp(1) + 20
    return(z)


