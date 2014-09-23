from cmath import exp
import numpy as np
import matplotlib.pyplot as plt

# This code calculates the intensity of light on a screen by integrating I(u,x)
# using Simpson's rule and plots it.

# Slit separation
sep = 20. * 1e-6 #m
# Number of slits
nslit = 10.
# Wavelength
wv = 500. * 1e-9 #m
# Screen width
swidth = 10. * 1e-2 #m
# Focal length
flength = 1.
# Total slit width
twidth = sep*nslit
# Alpha parameter
alpha = np.pi/sep

# Define the transmission function
def q(u):
	return np.sin(alpha*u)**2

# Define the integrand for intensity calculation
def I(u,x):
	ep = exp(2j*np.pi*x*u/(wv*flength))
	return np.sqrt(q(u))*ep

# Array of positions on the screen along axis of grating
xs = np.arange(0,swidth/2,1e-5)

# SIMPSON'S RULE INTEGRATION
# Number of subdivisions
N = 100
# Lower limit of integration
low = -twidth/2.
# Upper limit of integration
up = twidth/2.
# Width of a subdivision
h = (up-low)/N
# Empty array to hold results of integration
Is = np.array([])
# Compute integral for each position
for x in xs:
	s = I(low,x) + I(up,x)
	for k in range(1,N,2):
		s += 4*I(low+k*h,x)
	for k in range(2,N-1,2):
		s += 2*I(low+k*h,x)
	Is = np.append(Is,(1./3)*h*s)

# Calculate intensity
Is = abs(Is)**2

# Use symmetry to construct intensity for negative x
xtot = np.concatenate((-xs[::-1],xs))
Itot = np.concatenate((Is[::-1],Is))

# Plot result
plt.xlabel('Screen position [m]')
plt.ylabel('Intensity')
plt.title('Intensity of light through a diffraction grating on a screen.')
plt.plot(xtot,Itot)
plt.show()

