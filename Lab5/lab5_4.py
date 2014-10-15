import numpy as np
import matplotlib.pyplot as plt
import cmath as cm

###############################################################################

# This code calculates the intensity of light on a screen by finding the Fourier
# transform of the square root of the transmission function of light through a
# diffraction grating and plots the result.

################################## CONSTANTS ##################################

# Slit width
sw = 20.* 1e-6 #m
# Diffraction grating width
w = 200. * 1e-6 #m
# Padded width
W = 10.*w #m
# Wavelength of incident light
lam = 500. * 1e-9 #m
# Screen length
sl = 10. * 1e-2 #m
# Focal length
f = 1. #m

alpha = np.pi/sw #1/m


################################## FUNCTIONS ##################################

# A function to return the square root of the transmission function
def sqrtq(u):
	return np.sqrt(np.sin(alpha*u)**2)

################################## MAIN PROGRAM ##################################

# Define array of points along the grating
u = np.linspace(-w/2.,w/2.,100)

# Create a new array to hold padded points
nu = np.zeros(1000)
N = len(nu)
half = N/2.

# Insert the square root of the transmission function values half way through
# the new array, leave the rest of the values zero
for i in range(len(u)):
	nu[half+i] = sqrtq(u[i])

# Take the FFT of the sqrtq values
cks = np.fft.fft(nu)

# Transform these FFT coeffecients to intensity
I = (W/N)**2 * abs(cks)**2
# Reset main peak to the centre of the array
Is = np.roll(I,len(I)/2)
# Define an array that corresponds to the index of each ck value
k = np.arange(0,len(cks))
# Calculate the x poisition on the screen
x = (lam*f/W)*k
# Reset the x values to centre at x = 0
xs = x-x[N/2]

################################## PLOT ##################################

plt.plot(xs,Is)
plt.xlim(-sl/2.,sl/2.)
plt.xlabel('x [m]')
plt.ylabel('Intensity')
plt.title('Intensity of Light from a Diffraction Grating')
plt.show()
