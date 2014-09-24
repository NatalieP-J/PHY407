from gaussint import gaussint
import numpy as np

# This program computes the integral of x^3/(exp(x) - 1) from zero 
# to infinity for a number of sample points and detects the number of
# of sample points needed for the result to converge

# Set constants for program
# Number of sample points (an array to test convergence)
Ns = np.arange(50,101)
# Lower limit of integral
a = 0.
# Upper limit of integral
b = 1.

# Function returns z^3/(exp(z) - 1)dz under change of variables 
# z = x/(1-x). This makes the integration limits finite.
# multiply by 1 = e^-z/e^-z to eliminate overflow error
def Wintr(x):
	num = x**3*(np.exp(-x/(1-x))) # numerator
	den = (1-x)**5 * (1-np.exp(-x/(1-x))) # denominator
	return num/den

# Create array to hold results of integral calculations for each N
Wintgs = []
# Add arbitrary first value so recursive subtraction will work
Wintgs.append(0) 
# Return evaluation of integral for each number of sample points
# Check this result against the previous one to see if we have 
# acheieved convergence.

N = 0
while N < len(Ns):
	# required tolerance (if increasing N changes result by less than 
	# this, assume max accuracy acheived).
	eps = 1e-14
	Wintg = gaussint(Wintr,Ns[N],a,b) # value of integral for given N
	print 'N = {0}, integral = {1:.13f}'.format(Ns[N],Wintg) # print result
	diff = abs(Wintg - Wintgs[N-1]) # compare with previous result
	if diff < eps: # if difference is less than tolerance stop loop
		print 'Integral value converged at N = {0}'.format(Ns[N])
		N = len(Ns)
	elif diff > eps: # else, continue increasing N
		Wintgs.append(Wintg)
		N +=1
