import numpy as np
import matplotlib.pyplot as plt

# Function to return the forward difference derivative for chosen f, x and h
def fdiff(f,x,h):
	return (f(x+h)-f(x))/h

# Function to return the central difference derivative for chosen f, x and h
def cdiff(f,x,h):
	return (f(x+0.5*h) - f(x-0.5*h))/h

# Create array of step size values
hs = np.arange(-16.,3.)
hs = 10**hs

# Create arrays to hold output of numerical derivative functions
forw = np.zeros(len(hs))
cent = np.zeros(len(hs))

# Choose value of x at which to evaluate the derivative of sin(x)
xval = np.pi/4.

# Compute the true value of the derivative of sin(x) at xval
true = np.cos(xval)

# Compute the forward and central difference numerical derivatives 
# for various step sizes
for i in range(len(hs)):
	forw[i] = fdiff(np.sin,xval,hs[i])
	cent[i] = cdiff(np.sin,xval,hs[i])

# Find the error in the numerical estimates by subtracting the true value
# and taking the absolute value
ferr = abs(forw - true)
cerr = abs(cent - true)

# Plot the errors compared to the step size
plt.title('Absolute difference between numerical derivatives and true value for $sin(x)$ at $x = \pi/4$',fontsize = 20)
plt.xlabel('Step size (h)',fontsize = 20)
plt.ylabel('Error (estimate - true)',fontsize = 20)
plt.axvline(1e-8,linestyle='--',color = 'b',linewidth = 3,label = 'log10(h) = -8')
plt.axvline(1e-5,linestyle='--',color = 'g',linewidth = 3,label = 'log10(h) = -5')
plt.loglog(hs,ferr,'bo',markersize = 10,label = 'Forward difference method')
plt.loglog(hs,cerr,'g^',markersize = 10,label = 'Central difference method')
plt.legend(loc = 'best')
plt.show()