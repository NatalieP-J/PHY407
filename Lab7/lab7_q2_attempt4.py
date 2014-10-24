from __future__ import division
from math import sin,pi
from numpy import empty,array,arange
from pylab import plot,show
import numpy as np

a = 1.
b = 3.

def f(r):
    x,y = r
    dxdt = 1-(b+1)*x + a*y*x**2
    dydt = b*x - a*y*x**2
    #print dxdt,dydt
    return np.array([dxdt,dydt])

rdict = {}


def step(r,H,t,tend,delta,nmax):
    print 'r,t,H = ',r,t,H
    if t < tend:
        #print r
        r0 = r
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

        for n in range(2,nmax):
            #print n
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
                epsilon = (R1[m-1]-R2[m-1])/((float(n)/(float(n)-1))**(2*float(m))-1)
                #print epsilon
                R1[m] = R1[m-1] + epsilon
            error = np.sqrt(epsilon[0]**2 + epsilon[1]**2)
            if any(np.isinf(f(r1))) == True or any(np.isnan(f(r1))) == True or any(np.isinf(epsilon))==True or any(np.isnan(epsilon)) == True:
                error = 2*H*delta

        if error < H*delta:
            rdict[t+H] = R1[n-1]
            print 'rnew,tnew = ',R1[n-1],t+H
            return R1[n-1],t+H,H

        elif error >= H*delta:
            print 'Subdividing'
            print 'Part 1'
            step1 = step(r,H/2.,t,tend,delta,nmax)
            print 'step1 = ',step1
            rhalf,thalf,Hnew = step1
            print 'r1,t1 = ',rhalf,thalf
            print 'Part 2'
            rhalf2,thalf2,Hnew2 = step(rhalf,H/2.,t+H/2.,tend,delta,nmax)
            print 'r2,t2 = ',rhalf2,thalf2
    # Set r equal to the most accurate estimate we have,
    # before moving on to the next big step
    #if t < tend and t in rdict:
    #    return r,t+H
    elif t >= tend:
        return rdict

tstart = 0.0
tend = 20.0
N = 1.          # Number of "big steps"
H = (tend-tstart)/N      # Size of "big steps"
delta = 1e-10    # Required position accuracy per unit time
#delta = 1e-1
nmax = 8

x0 = 0.0
y0 = 0.0

rpts = []
r = array([x0,y0],float)

rdict[tstart] = r

print step(r,H,tstart,tend,delta,nmax)

'''
t = tstart
# Do the "big steps" of size H
#for t in tpoints:

#    rpts.append(r)

    

# Plot the results
plot(tpoints,rpts)
plot(tpoints,rpts,"b.")
show()
'''