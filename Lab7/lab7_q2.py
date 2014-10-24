from __future__ import division
from math import pi
from numpy import empty,array,arange
import matplotlib.pyplot as plt

###############################################################################

# This code computes the concentration of two chemicals in a Brusselator
# chemical oscillator over time. It does this by recursively evaluating the
# Bulirsch - Stoer Method until a desired accuracy in each step is reached.

# This version has been modified from bulirsch.py provided with the
# Computational Physics textbook by Mark Newman and contains some of his 
# original comments.

################################## CONSTANTS ##################################

# Set Brusselator constants
a = 1.
b = 3.

################################## FUNCTIONS ##################################

# The Brusselator function, returns the time derivatives of x and y
# concentrations given x and y

def f(r):
    x,y = r
    dxdt = 1 - (b+1)*x + a*x**2*y
    dydt = b*x - a*x**2*y
    return array([dxdt,dydt],float)

# Create arrays to hold results of step
rsolnpts = []
tsolpts = []

# This function does a step in the Bulirsch-Stoer method
def step(r,t,H,nmax,delta):
    '''
    r - a length 2 vector containing x and y concentration
    t - time
    H - big step size
    nmax - maximum depth of Richardson extrapolation before subdivision
    delta - a parameter, which when multiplied by H specifies desired accuracy
    '''
    # Do one modified midpoint step to get things started
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)

    # The array R1 stores the first row of the
    # extrapolation table, which contains only the single
    # modified midpoint estimate of the solution at the
    # end of the interval
    R1 = empty([1,2],float)
    R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))

    # Now increase n until the required accuracy is reached
    # or until the maximum extrapolation depth reached
    error = 2*H*delta
    for n in range(2,nmax):

        h = H/n

        # Modified midpoint method
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for i in range(n-1):
            r1 += h*f(r2)
            r2 += h*f(r1)

        # Calculate extrapolation estimates.  Arrays R1 and R2
        # hold the two most recent lines of the table
        R2 = R1
        R1 = empty([n,2],float)
        R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))
        for m in range(1,n):
            epsilon = (R1[m-1]-R2[m-1])/((n/(n-1))**(2*m)-1)
            R1[m] = R1[m-1] + epsilon
        error = (epsilon[0]**2 + epsilon[1]**2)**0.5 

        # If we have reached desired accuracy, return x and y
        # estimate and the updated time.
        if error < H*delta:
            rsolnpts.append(R1[n-1])
            tsolpts.append(t+H)
            return R1[n-1],t + H

    # If target accuracy was not reached before extrapolation
    # depth was exceeded, divide the current interval into 
    # two halves and evaluate for both.
    rhalf,thalf = step(r,t,H/2.,nmax,delta)
    rhalf2,thalf2 = step(rhalf,t+H/2.,H/2.,nmax,delta)
    return rhalf2,thalf2

################################## MAIN PROGRAM ##################################

# Set specific conditions for the program
tstart = 0.0 # Start time
tend = 20.0 # End time
H = 20.0 # Initial interval size
delta = 1e-10 # Required accuracy per unit time
nmax = 8 # Maximum Richardson extrapolation depth

# Set initial concentrations
x0 = 0.0 
y0 = 0.0
# Form initial value vector
r = array([x0,y0],float)

t = tstart
# Evaluate x(t) and y(t) on desired interval
while t < tend:
    r,t = step(r,t,H,nmax,delta)
rsolnpts = array(rsolnpts)

# Divide the vector back into x and y concentrations
xsolnpoints = rsolnpts[:,0]
ysolnpoints = rsolnpts[:,1]

################################## PLOT ##################################
plt.figure()
plt.plot(tsolpts,xsolnpoints,label = 'x concentration')
plt.plot(tsolpts,xsolnpoints,"b.")
plt.plot(tsolpts,ysolnpoints,label = 'y concentration')
plt.plot(tsolpts,ysolnpoints,"g.")
plt.legend(loc = 'best')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Evolution of chemical concentrations in a Brusselator system')
plt.show()