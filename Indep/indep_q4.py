import numpy as np
from gaussxw import gaussxwab
import matplotlib.pyplot as plt
from scipy.special import jn_zeros

N = 100
b = np.pi
a = 0

taus,weights = gaussxwab(N,b,a)

R = 10.
T0 = 50.
c = 1.25

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

def J1int(tau,x):
	return np.cos(tau-x*np.sin(tau))

def J1(x):
	return (1./np.pi)*gaussint(J1int,taus,weights,args = x)

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

def findlambda(nterms,tol):
	lambdas = []
	for n in range(1,nterms+1):
		loc = approxzero(n)
		init = [loc,loc+0.1]
		lambdas.append(secant(init,J0,tol))
	return np.array(lambdas)/R

def heatfn(t,lams,nterms,J0vals,J1vals):
	heat = np.zeros(np.shape(J0vals[0]))
	for n in range(nterms):
		heat += (np.exp(-c*t*lams[n]**2)/(lams[n]*R))*(J0vals[n]/J1vals[n])
	return 2*T0*heat

xmin = 0
xmax = R
delx = 0.01
x = np.arange(xmin,xmax+delx,delx)
tmin = 0
tmax = 100.
delt = 0.5
t = np.arange(tmin,tmax+delt,delt)
N = 50
tol = 1e-9
lams1 = findlambda(N,tol)
lams2 = jn_zeros(0,N)
masterx1 = np.zeros((len(lams1),len(x)))
masterx2 = np.zeros((len(lams2),len(x)))
for i in range(len(lams1)):
	masterx1[i] = lams1[i]*x
	masterx2[i] = lams2[i]*x

J0vals1 = J0(masterx1)
J0vals2 = J0(masterx2)
J1vals1 = J1(lams1*R)
J1vals2 = J1(lams2*R)
u1 = heatfn(0,lams1,N,J0vals1,J1vals1)
u2 = heatfn(0,lams2,N,J0vals2,J1vals2)

# Set up animation
plt.figure()
# Choose axes
ax = plt.axes(xlim = (xmin,xmax),ylim=(0,T0+0.1*T0))
line = ax.plot(x,u1)
for i in range(1,len(t)):
	unew = heatfn(t[i],lams1,N,J0vals1,J1vals1)
	line[0].set_ydata(unew)
	ax.set_title('t = {0} s'.format(i*delt))
	plt.draw()

plt.figure()
plt.subplot(411)
plt.plot(x,u1)
plt.ylim(0,60)
plt.subplot(412)
plt.plot(x,heatfn(0.005,lams1,N,J0vals1,J1vals1))
plt.ylim(0,60)
plt.subplot(413)
plt.plot(x,heatfn(10,lams1,N,J0vals1,J1vals1))
plt.ylim(0,60)
plt.subplot(414)
plt.plot(x,heatfn(100,lams1,N,J0vals1,J1vals1))
plt.ylim(0,60)

#J0vals = J0()

