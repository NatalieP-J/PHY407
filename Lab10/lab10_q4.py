import numpy as np
from random import random,seed
from numpy.linalg import norm

###############################################################################

# This code computes the volume of a sphere in 10 dimensions using the Mean 
# Value Monte Carlo method

################################## CONSTANTS ##################################

# Choose seed
seed(42)
# Number of dimensions
sphdim = 10
# Limits of sphere in each dimension
sphlims = [-1,1]
# Radius of sphere
radius = 1.
# Number of points to use in integration
npts = int(1e6)

################################## FUNCTIONS ##################################

# Returns 1 if r vector is within the sphere, 0 if it is without
def f(r,radius):
	if norm(r) < radius:
		return 1
	if norm(r) >= radius:
		return 0

# Create an array of random numbers with length size, scaling each component
def getx(size,scale):
	r = np.array([])
	m = abs(scale[0]-scale[1])
	c = scale[0]
	for i in range(size):
		r = np.append(r,m*random() + c)
	return r

################################## MAIN PROGRAM ##################################

# Initialize average of f and f^2 as zero
favg = 0
f2avg = 0

# Create random number array
r = np.zeros(10,npts)

# Create npts points and evaluate f and f^2 at each point
for i in range(npts):
	if np.mod(i,npts/50) == 0:
		print '{0} points'.format(i)
	# Find random vector
	r = getx(sphdim,sphlims)
	# Update average of f
	favg += f(r,radius)
	# Update average of f^2
	f2avg += f(r,radius)**2

# Divide by the total number of points to find the true average
favg *= (1/float(npts))
f2avg *= (1/float(npts))

# Compute the variance and with this, the error
varf = f2avg - favg**2
err = (2**sphdim)*(varf/float(npts))**0.5

# Compute the value of the integral
I = (2**sphdim)*favg

# Print the results
print 'I = ',I,'p/m',err