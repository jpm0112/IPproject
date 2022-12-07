
import numpy as np

# Ackley function


def evaluate_ackley(list):
    x= list[0]
    y = list[1]
    z1 = -20.0* np.exp(-0.2*np.sqrt(0.5* (x**2 + y**2)))
    z2= - np.exp(0.5* (np.cos(2*np.pi*x) + np.cos(2*np.pi*y)))
    z = z1 + z2 + np.exp(1) + 20
    return(z)


#Definition Bohachevsky Function 

def evaluate_bona(x):
    return x[0]**2+2*(x[1]**2)-0.3*np.cos(3*np.pi*x[0])-0.4*np.cos(4*np.pi*x[1])+0.7



#Definition Three-hump camel function

def evaluate_threecamel(x):

    return 2*x[0]**2-1.05*(x[0]**4)+(x[0]**6)/6+x[0]*x[1]+x[1]**2

#Gradient of Ackley Function 

def evaluate_d_ackley(x):

    return np.array([(20*0.2*np.sqrt(0.5)*x[0]*np.exp((-  (0.2*np.sqrt(0.5)))*np.sqrt(x[0]**2+x[1]**2)))/np.sqrt(x[0]**2+x[1]**2)+np.pi*np.sin(2*np.pi*x[0])*np.exp(0.5*(np.cos(2*np.pi*x[0])+np.cos(2*np.pi*x[1]))),

                      (20*0.2*np.sqrt(0.5)*x[1]*np.exp((-(0.2*np.sqrt(0.5)))*np.sqrt(x[0]**2+x[1]**2)))/ np.sqrt(x[0]**2+x[1]**2)+np.i*np.sin(2*np.pi*x[1])*np.exp(0.5*(np.os(2*np.pi*x[0])+np.cos(2*np.pi*x[1])))])



#Gradient of Bohachevsky Function

def evaluate_d_bona(x):

    return np.array([2*x[0]+0.9*np.pi*np.sin(3*np.pi*x[0]), 4*x[1]+1.6*np.pi*np.sin(4*np.pi*x[1])])



#Gradient of Three-hump camel function

def evaluate_d_threecamel(x):

    return np.array([x[0]**5-4.2*x[0]**3+4*x[0]+x[1],x[0]+2*x[1]])