import numpy as np
from gaussxw import gaussxwab
import matplotlib.pyplot as plt

###############################################################################

# This code animates the temperature in a cylinder as a function of radius over
# time.

################################## CONSTANTS ##################################

Nint = 100 # Number of subintervals for Gaussian integration
b = np.pi # Upper bound of Bessel function integral
a = 0 # Lower bound of Bessel function integral

# Generate points and weights for Gaussian integration
taus,weights = gaussxwab(Nint,a,b)

# Set parameters for the cylinder
R = 10. # Radius of the cylinder
T0 = 50. # Initial temperature of the cylinder
c = 1.25 # Speed at which heat change propagates through the cylinder

################################## FUNCTIONS ##################################

def gaussint(fn,tau,w,args = False):
    """
    Returns the integral of fn from lowlim to uplim using Gaussian 
    quadrature with Nsamp sample points.
    """ 
    s = np.zeros(np.shape(args))
    for i in range(len(tau)):
        s += w[i]*fn(tau[i],args) # evaluate fn at points and weight it
    return s

# Integrand to compute the 0th order Bessel function of the first kind
def J0int(tau,x):
    return np.cos(x*np.sin(tau))

# Returns the 0th order Bessel function of the first kind evaluated at x
def J0(x):
    return (1./np.pi)*gaussint(J0int,taus,weights,args = x)

# Integrand to compute the 1st order Bessel function of the first kind
def J1int(tau,x):
	return np.cos(tau-x*np.sin(tau))

# Returns the 1st order Bessel function of the first kind evaluated at x 
def J1(x):
	return (1./np.pi)*gaussint(J1int,taus,weights,args = x)

# Based on guess initial, this function returns the location of the nearest
# zero of fn to a precision tol
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

# Return the approximate location of the nth zero of the 0th order Bessel
# function of the first kind
def approxzero(n):
    return np.pi*(n-0.25)

# Find the first nterms zeros of J0 to precision tol
def findlambda(nterms,tol):
	zerolocs = []
	for n in range(1,nterms+1):
		loc = approxzero(n) #Use approximation scheme for initial guess
		init = [loc,loc+0.1]
		zerolocs.append(secant(init,J0,tol))
	return np.array(zerolocs)/R

# Return the temperature profile at time t with
# Requires a time t, a list of zero locations lams, a 2D array where each row
# is J0(lams[i]*x) and a 1D array J1(lams*R) 
def heatfn(t,lams,J0vals,J1vals):
	heat = np.zeros(np.shape(J0vals[0])) # Initialize sum
	for n in range(len(lams)): # Sum over chosen number of terms
		heat += (np.exp(-c*t*lams[n]**2)/(lams[n]*R))*(J0vals[n]/J1vals[n])
	return 2*T0*heat

################################## MAIN PROGRAM ##################################

# Generate array in radius
xmin = 0
xmax = R
delx = 0.01
x = np.arange(xmin,xmax+delx,delx)

# Generate array in time
tmin = 0
tmax = 100.
delt = 0.5
t = np.arange(tmin,tmax+delt,delt)

# Find zeros and evaluate J0, J1 and appropriate locations
N = 50 # Number of terms in the sum

tol = 1e-9 # Tolerance with which to find zeros
lams = findlambda(N,tol)  # Find zeros

masterx = np.zeros((len(lams),len(x))) # Create array to feed to J0
for i in range(len(lams)):
	masterx[i] = lams[i]*x # Fill in array

# Generate J0 and J1 to be used for all time
J0vals = J0(masterx)
J1vals = J1(lams*R)
# Compute the intial heat function
u0 = heatfn(0,lams,J0vals,J1vals)

# Set up animation
plt.figure()
# Choose axes
ax = plt.axes(xlim = (xmin,xmax),ylim=(0,T0+0.1*T0))
# Start with initial heat function
line = ax.plot(x,u0)
plt.xlabel('Radius')
plt.ylabel('Temperature')
# Loop over time, animating as you go
for i in range(1,len(t)):
	unew = heatfn(t[i],lams,J0vals,J1vals)
	line[0].set_ydata(unew)
	ax.set_title('t = {0} s'.format(i*delt))
	plt.draw()

################################## PLOT ##################################

# Create a plot of our snapshots
plt.figure()
plt.title('Temperature in a cylinder as a function of radius')
plt.plot(x,u0,label = 't = 0')
plt.plot(x,heatfn(0.005,lams,J0vals,J1vals),label = 't = 0.005')
plt.plot(x,heatfn(10,lams,J0vals,J1vals),label = 't = 10')
plt.plot(x,heatfn(80,lams,J0vals,J1vals),label = 't = 80')
plt.ylim(0,60)
plt.xlabel('Radius')
plt.ylabel('Temperature')
plt.legend(loc = 'best')

