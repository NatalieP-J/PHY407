import numpy as np
import matplotlib.pyplot as plt

###############################################################################

# This code deconvolves a blurry image with a Gaussian point spread function to 
# produce an less blurry image using the Fourier transform coefficients of the 
# blurry image and PSF and convolution theorem.

################################## CONSTANTS ##################################

sigma = 25.
eps = 10**-3

################################## LOAD DATA ##################################

blur = np.loadtxt('blur.txt')

################################## FUNCTION ##################################

# Function to produce a 2D Gaussian with its peaks in the four corners of the 
# array

def gauss2D(rows,cols,sigma):
	gauss = np.zeros((rows,cols))
	for i in range(rows):
		ip = i
		# If ip is half way through row indices, shift it to negative
		if ip > rows/2:
			ip -= rows
		for j in range(cols):
			jp = j
			# If jp is half way through column indices, shift it to negative
			if jp > cols/2:
				jp -= cols
			gauss[i][j] = np.exp(-(ip**2 + jp**2)/(2.*sigma**2))
	return gauss

################################## MAIN PROGRAM ##################################

# Determine the shape desired for the 2D Gaussian PSF
rows = len(blur)
cols = len(blur[0])

# Calculate the PSF
psf = gauss2D(rows,cols,sigma)

# Get the Fourier transform of the blurry data and the psf
fblur = np.fft.rfft2(blur)
fpsf = np.fft.rfft2(psf)

# Create an empty array to hold divided Fourier coefficients (and specify complex)
funblur = np.zeros(fblur.shape,complex)

# Find the indices where abs(fpsf) >= eps and where abs(fpsf) < eps
geps = np.where(abs(fpsf) >= eps)
leps = np.where(abs(fpsf) < eps)

# To avoid division by zero error, divide by the psf coefficients are
# sufficiently large
funblur[geps] = fblur[geps]/fpsf[geps]
funblur[leps] = fblur[leps]

# Inverse Fourier transform to get the result
unblur = np.fft.irfft2(funblur/(rows*cols))

################################## PLOT ##################################
plt.gray()
plt.axis('off')
plt.imshow(unblur)
plt.title('Deconvolved Image')
plt.show()
