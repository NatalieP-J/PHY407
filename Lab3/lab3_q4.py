import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
# Set constants for the code
# Light striking angle
phi =-np.pi/4.
# Separation between grid points
h1 = 30000.
# Separation to be used for central differences
h2 = 2*h1

# Function returns intensity given the partial derivatives of height (w)
# in the x and y directions
def inten(dwdx,dwdy):
	num = np.cos(phi)*dwdx + np.sin(phi)*dwdy
	den = np.sqrt((dwdx**2) + (dwdy**2) + 1)
	return num/den

def gridpartials(alt):
	"""
	Returns the partial derivative of alt at every point in the grid in 
	the 'row'-direction.
	Loops sthrough every row, then loops through each point in the row
	Calculates the derivative at each point.
	If it is an end point, uses the forward or backward difference method
	as approriate. Otherwise, uses the central difference method (but with
	double the separation, as we take points from both sides of the point
	of interest, not just one).
	"""
	# Create array with same shape as initial data to hold partial 
	# derivative results
	deriv = np.zeros(alt.shape)
	for i in range(len(alt)):
		for k in range(len(alt[i])):
			if k == 0:
				deriv[i][k] = (alt[i][k+1] - alt[i][k])/h1 # forward
			if k == (alt.shape[1] - 1):
				deriv[i][k] = (alt[i][k] - alt[i][k-1])/h1 # backward
			else:
				deriv[i][k] = (alt[i][k+1] - alt[i][k-1])/h2 # central
	return deriv


# w values on the grid points
alt = np.loadtxt('altitude.txt')
# transpose of the above will be used for calculating y derivatives
altT = np.transpose(alt)

# For x derivative, this is already the 'row'-direction, so use 
# grid partials
dwdx = gridpartials(alt)

# For y derivatives - cycling through the rows of the transpose is 
# equivalent to looping through columns in the original 2D array.
# Cycling through rows so use grid partials
dwdy = gridpartials(altT)
dwdy = np.transpose(dwdy)

# Calculate intensities at each point on the grid
I = inten(dwdx,dwdy)

# Plot intensities on the grid (rescaled slightly to clarify image)
plt.gray()
plt.axis('off')
plt.title('Intensity of light on the earth for a striking angle of 45 degrees')
plt.imshow(I,vmax = 0.03,vmin = -0.03,cmap = cm.gray_r)
