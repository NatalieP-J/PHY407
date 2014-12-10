import numpy as np
from scipy.special import jn_zeros
from gaussxw import gaussxwab

N = 100
b = np.pi
a = 0

taus,weights = gaussxwab(N,b,a)

def gaussint(fn,x,w,args = False):
    """
    Returns the integral of fn from lowlim to uplim using Gaussian 
    quadrature with Nsamp sample points.
    """ 
    s = np.zeros(np.shape(args))
    for i in range(len(x)):
        s += w[i]*fn(x[i],args) # evaluate fn at points and weight it
    return s

def J0int(tau,x):
    return np.cos(x*np.sin(tau))

def J0(x):
    return (1./np.pi)*gaussint(J0int,taus,weights,args = x)

def secant(initial,fn,tol):
    x1,x2 = initial
    while True:
        # Find slope of secant line connecting x1 and x2
        fprime = (fn(x2) - fn(x1))/(x2-x1) 
        # Find where current secant intersects the x-axIs
        x3 = x2 - fn(x2)*(1./fprime)
        # If accuracy not achieved, update x1 and x2 and try again
        if abs(x3 - x2) > tol:
            x1 = x2
            x2 = x3
        # If accuracy achieved, break the loop
        elif abs(x3 - x2) < tol:
            break
    return x3

def approxzero(n):
    return np.pi*(n-0.25)

tol = 1e-5 

inits = [[1.0,1.5],[4.5,5.0],[8.0,8.5],[11.0,11.5],[14.0,14.5]]
zeros = []
for i in range(len(inits)):
    zeros.append(secant(inits[i],J0,tol))

zeros = np.array(zeros)
sci = jn_zeros(0,5)



