import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

# This code finds the temperature for which the effeciency of a light bulb is
# maximized, using a golden ratio search

# Set constants for the program
# Planck's constant
h = 6.62606957 * 1e-34 #m^2 kg s^-1
# Speed of light
c = 3.000 * 1e8 #m s^-1
# Boltzmann constant
kB = 1.3806488 * 1e-23 #m^2 kg s^-1 K^-1
# Lower wavelength limit of visible light
wv1 = 390 * 1e-9 #m
# Upper wavelength limit of visible light
wv2 = 750 * 1e-9 #m
# Golden ratio
z = 0.5 + np.sqrt(5)/2.
# Choose number of sample points for Gaussian quadrature
Nsamp = 100

# Define a function to hold integrand of equation for eta
def etaint(x):
    return x**3/(np.exp(x) - 1)

# Define a function that will calculate -eta, given a temperature T,
# a set of Gaussian quadrature points xs and weights ws
def neta(T,args):
    xs,ws = args
    a = h*c/(wv2*kB*T) # lower limit
    b = h*c/(wv1*kB*T) # upper limit
    x = 0.5*(b-a)*xs + 0.5*(b+a) # scale points
    w = 0.5*(b-a)*ws # scale weights
    eta = 0 # start integration sum 
    for n in range(Nsamp):
        eta += w[n]*etaint(x[n])
    eta *= (15./np.pi**4)
    return -eta

# A function to find an x2 for the golden ratio search, given x1 and x4
def getx2(x1,x4):
    return x4 - (x4-x1)*(1./z)

# A function to find an x3 for the golden ratio search, given x1 and x4
def getx3(x1,x4):
    return x1 + (x4-x1)*(1./z)

# A function to evaluate another function depending on whether or not
# it has multiple arguments (used in golden_min)
def feval(fn,vals,args):
    x1,x2,x3,x4 = vals
    if args == False:
        return fn(x1),fn(x2),fn(x3),fn(x4)
    elif args != False:
        return fn(x1,args),fn(x2,args),fn(x3,args),fn(x4,args)

# Finds the minima of fn within region brackets by the points given as
# initial and to accuracy tol. If the function has more than one 
# argument they are listed in args.
def golden_min(initial,fn,tol,args = False):
    x1,x4 = initial
    x2,x3 = getx2(x1,x4),getx3(x1,x4)
    i = 0
    while True: 
        f1,f2,f3,f4 = feval(fn,[x1,x2,x3,x4],args)
        if x4 - x1 > tol:
            if f2 < f3:
                x4 = x3
                x3 = x2
                x2 = getx2(x1,x4)
            if f3 < f2:
                x1 = x2
                x2 = x3
                x3 = getx3(x1,x4)
        elif x4 - x1 < tol:
            break
    return x1 + (x4-x1)/2.               

# Import Gaussian weights and points for an interval from -1 to 1
xs,ws = gaussxw(Nsamp)

# Specify target accuracy of 1 K
eps = 1.

# Decide bracketing region based on temperature plot from lab4_q6a
T1 = 6000
T4 = 8000

# Call golden min to find the minimum of the negative effeciency
Tf = golden_min([T1,T4],neta,eps,args = [xs,ws])

print 'Maximum effeciency occurs at T = ',Tf,'K'

