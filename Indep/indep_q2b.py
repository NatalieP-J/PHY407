from scipy.special import jn,gamma
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from math import factorial
from gaussxw import gaussxwab

def gaussint(fn,Nsamp,lowlim,uplim,args = False):
	"""
	Returns the integral of fn from lowlim to uplim using Gaussian 
	quadrature with Nsamp sample points.
	"""
	x,w = gaussxwab(Nsamp,lowlim,uplim) # gets points and weights
	s = np.zeros(np.shape(args))
	for i in range(Nsamp):
		s += w[i]*fn(x[i],args) # evaluate fn at points and weight it
	return s

def J0sum(x,kmax):
	Jval = np.zeros(np.shape(x))
	for k in range(kmax):
		Jvaladd = (((-1.)**k)/(float(factorial(k))**2))*(x/2.)**(2*k)
		Jval += Jvaladd
	return Jval

def J0int(tau,x):
	return np.cos(x*np.sin(tau))

xmin = 0
xmax = 20
step = 0.01
kmax = 75
x = np.arange(xmin,xmax+step,step)

a = 0
b = np.pi
N = 100

J0_integral = (1./np.pi)*gaussint(J0int,N,a,b,args = x)
J0_sum = J0sum(x,kmax)
sci = jn(0,x)

plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[2.5, 1]) 
plt.subplot(gs[0])
plt.plot(x,J0_integral,label = 'Integral method')
plt.plot(x,J0_sum,label = 'Sum method')
plt.hlines(0,xmin,xmax)
plt.legend(loc = 'best')
plt.xlim(xmin,xmax)
plt.subplot(gs[1])
plt.plot(x,abs(sci-J0_integral))
plt.plot(x,abs(sci-J0_sum))
plt.xlim(xmin,xmax)
plt.ylim(-max(abs(sci-J0_sum)),max(abs(sci-J0_sum)))
plt.show()