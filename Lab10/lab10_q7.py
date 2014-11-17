import numpy as np
from random import random,seed
from numpy.linalg import norm
import matplotlib.pyplot as plt

###############################################################################

# This code computes the value of an integral in 1 dimension using the Mean 
# Value Monte Carlo method

################################## CONSTANTS ##################################

# Choose seed
seed(42)
# Lower limit of integration
a = 0
# Upper limit of integration
b = 1
# Number of points used to evaluate the integral
npts = int(1e4)
# Number of times to evaluate the integral
iterr = 100
# Value of weighting function evaluated over interval
wint = 2

################################## FUNCTIONS ##################################

# Integrand
def fw(r):
	return 1./(np.exp(r) + 1)

################################## MAIN PROGRAM ##################################

# Initialize average of f and f^2 as zero
fwavg = 0
fw2avg = 0

# Initialize arrays to results over the iterations
Is = np.zeros(iterr)
errs = np.zeros(iterr)

for k in range(iterr):
	# Create npts points and evaluate f and f^2 at each point
	for i in range(npts):
		# Find a random number in the integration range
		r = (abs(a-b)*random()+a)**2
		# Update average of f
		fwavg += fw(r)
		# Update average of f^2
		fw2avg += fw(r)**2

	# Find true averages by dividing by the total number of points used
	fwavg *= (1./float(npts))
	fw2avg *= (1./float(npts))

	# Compute the variance and from this the error
	varfw = fw2avg - fwavg**2
	err = wint*(varfw/float(npts))**0.5

	# Compute the true value of the integral
	I = wint*fwavg

	Is[k] = I
	errs[k] = err

################################## PLOT ##################################

plt.figure()
plt.hist(Is,10,range = [0.8,0.88])
plt.xlabel('Integral Value')
plt.ylabel('Number of Iterations')
plt.title('Value of intgeral via the Mean Value Monte Carlo Method with Importance Sampling')
plt.xlim(0.8,0.88)
plt.show()