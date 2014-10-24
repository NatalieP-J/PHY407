from __future__ import division
from math import pi
from numpy import empty,array,arange
import matplotlib.pyplot as plt

a = 1.
b = 3.

tstart = 0.0
tend = 20.0
N = 1#1000          # Number of "big steps"
H = (tend - tstart)/N      # Size of "big steps"
delta = 1e-10    # Required position accuracy per unit time
nmax = 8

def f(r):
    x,y = r
    dxdt = 1 - (b+1)*x + a*x**2*y
    dydt = b*x - a*x**2*y
    return array([dxdt,dydt],float)

rsolnpts = []
tsolpts = []

def step(r,t,H):
    print 'r,t,H = ',r,t,H
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
        if error < H*delta:
            #print 'error = ',error
            #print 'rnew,tnew,Hnew = ',R1[n-1], t+H,H
            rsolnpts.append(R1[n-1])
            tsolpts.append(t+H)
            return R1[n-1],t + H
    #print r,t,H
    rhalf,thalf = step(r,t,H/2.)
    rhalf2,thalf2 = step(rhalf,t+H/2.,H/2.)
    return rhalf2,thalf2

x0 = 0.0
y0 = 0.0
r = array([x0,y0],float)

t = tstart

# Do the "big steps" of size H
while t < tend:
    r,t = step(r,t,H)
rsolnpts = array(rsolnpts)

xsolnpoints = rsolnpts[:,0]
ysolnpoints = rsolnpts[:,1]

# Plot the results
plt.plot(tsolpts,xsolnpoints)
plt.plot(tsolpts,xsolnpoints,"b.")
plt.plot(tsolpts,ysolnpoints)
plt.plot(tsolpts,ysolnpoints,"g.")
plt.figure()
plt.plot(xsolnpoints,ysolnpoints)
plt.show()