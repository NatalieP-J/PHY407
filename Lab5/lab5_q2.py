import numpy as np
import matplotlib.pyplot as plt

###############################################################################

# This program calculates the Fourier transform of a square wave with 1000
# coefficients, then discards all but the first 10 to approximate the wave

################################## FUNCTIONS ##################################

def f(x):
	fs = []
	for i in range(len(x)):
		if np.mod(np.floor(2*x[i]),2) == 0: # if floor(2x) is even
			fs.append(1)
		elif np.mod(np.floor(2*x[i]),2) != 0: # if floor(2x) is odd
			fs.append(-1)
	return fs

################################## MAIN PROGRAM ##################################

# Number of samples
N = 1000

# Create N sample points between 0 and 1 (one cycle of the wave)
n = np.linspace(0,1,N)

# Find the Fourier coefficients
cks = np.fft.rfft(f(n))

# Choose a number after which coefficients are ejected
eject = 10

# For coefficients above this number, set them to zero
cks[eject:] = 0

# Inverse Fourier transform to determine the approximation
f_new = np.fft.irfft(cks)

n_new = np.linspace(0,1,len(f_new))


################################## PLOT ##################################

plt.plot(n,f(n),linewidth = 4,label = 'Original Function')
plt.plot(n_new,f_new,linewidth = 3,label = '10 Coeffecient Fourier Series')
plt.title('Fourier Series Approximation of a Square Wave')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-1.5,1.5)
plt.legend(loc = 'best')
plt.show()
