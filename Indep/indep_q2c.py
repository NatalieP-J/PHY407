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

def J1int(tau,x):
	return np.cos(tau - x*np.sin(tau))

xmin = 0
xmax = 40
step = 0.01
kmax = 50
x = np.arange(xmin,xmax+step,step)

a = 0
b = np.pi
N = 100

J1_integral = (1./np.pi)*gaussint(J1int,N,a,b,args = x)
sci = jn(1,x)

plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[2.5, 1]) 
plt.subplot(gs[0])
plt.plot(x,J1_integral,label = 'Integral method')
plt.plot(x,sci,label = 'Scipy module')
plt.legend(loc = 'best')
plt.xlim(xmin,xmax)
plt.subplot(gs[1])
plt.plot(x,abs(sci-J1_integral))
plt.xlim(xmin,xmax)
plt.ylim(-max(abs(sci-J1_integral)),max(abs(sci-J1_integral)))
plt.show()