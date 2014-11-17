import numpy as np
from random import random,seed
from numpy.linalg import norm

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

################################## FUNCTIONS ##################################

# Integrand
def f(r):
	return (r**-0.5)/(np.exp(r) + 1)

################################## MAIN PROGRAM ##################################

# Initialize average of f and f^2 as zero
favg = 0
f2avg = 0

Is = []
errs = []
for k in range(iterr):
	# Create npts points and evaluate f and f^2 at each point
	for i in range(npts):
		# Find a random number in the integration range
		r = abs(a-b)*random()+a
		# Update average of f
		favg += f(r)
		# Update average of f^2
		f2avg += f(r)**2

	# Find true averages by dividing by the total number of points used
	favg *= (1/float(npts))
	f2avg *= (1/float(npts))

	# Compute the variance and from this the error
	varf = f2avg - favg**2
	err = (b-a)*(varf/float(npts))**0.5

	# Compute the true value of the integral
	I = (b-a)*favg

	Is.append(I)
	errs.append(err)

################################## PLOT ##################################

plt.figure()
plt.hist(Is,10,range = [0.8,0.88])
plt.xlabel('Iteration')
plt.ylabel('Intergral Value')
plt.title('Value of intgeral via the Mean Value Monte Carlo')
plt.show()