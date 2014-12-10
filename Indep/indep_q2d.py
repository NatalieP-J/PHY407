from scipy.special import jn,gamma
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from math import factorial
from gaussxw import gaussxwab
plt.ion()

###############################################################################

# This code uses the integral form of the Bessel functions to find J0

################################## CONSTANTS ##################################

Nint = 100 # Number of subintervals for Gaussian integration
b = np.pi # Upper bound of Bessel function integral
a = 0 # Lower bound of Bessel function integral

################################## FUNCTIONS ##################################

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

# Integrand to find J0
def J0int(tau,x):
	return np.cos(x*np.sin(tau))

################################## MAIN PROGRAM ##################################

# Create array in independent variable x
xmin = 0
xmax = 20
step = 0.01
x = np.arange(xmin,xmax+step,step)

# Evaluate J0 on chosen x range
J0_integral = (1./np.pi)*gaussint(J0int,Nint,a,b,args = x)
# Find the scipy J0 function
sci = jn(0,x)

################################## PLOT ##################################

# Make a plot comparing sci and J0_integral and include a subplot with
# residuals between the two.
plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[2.5, 1]) 
plt.subplot(gs[0])
plt.plot(x,J0_integral,label = 'Integral method')
plt.plot(x,sci,label = 'Scipy module')
plt.title('Bessel function $J_0$',fontsize = 20)
plt.ylabel('$J_0(x)$',fontsize = 20)
plt.legend(loc = 'best')
plt.xlim(xmin,xmax)
plt.subplot(gs[1])
plt.plot(x,abs(sci-J0_integral))
plt.ylabel('Residuals')
plt.xlabel('x')
plt.xlim(xmin,xmax)
plt.ylim(0,max(abs(sci-J0_integral)))
plt.show()