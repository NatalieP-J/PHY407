from gaussint import gaussint
import numpy as np

# This program computes the integral of x^3/(exp(x) - 1) from zero 
# to infinity for a number of sample points

# Set constants for program
# Number of sample points (an array to test convergence)
Ns = np.arange(50,101)
# Lower limit of integral
a = 0.
# Upper limit of integral
b = 1.

# Function returns z^3/(exp(z) - 1)dz under change of variables 
# z = x/(1-x). This makes the integration limits finite.
def Wintr(x):
	num = x**3 # numerator
	den = (1-x)**5 * (np.exp(x/(1-x))-1) # denominator
	return num/den

# Return evaluation of integral for each number of sample points
for N in Ns:
	Wintg = gaussint(Wintr,N,a,b)
	print 'N = {0}, integral = {1:.14f}'.format(N,Wintg)