import numpy as np

# This code finds the L1 Lagrange point for the Earth-Moon system using
# the secant root finding method.

# Set constants for the code
# Gravitational constant
G = 6.674 * 1e-11 #m^3 kg^-1 s^-2
# Mass of Earth
M = 5.974 * 1e24 #kg
# Mass of the Moon
m = 7.348 * 1e22 #kg
# Distance between the Earth and the Moon
R = 3.844 * 1e8 #m
# Angular velocity of the Moon about the Earth
w = 2.662 * 1e-6 #s^-1

# Define the function for which L1 is a root
def f(r):
	return (G*M/r**2) - (G*m/(R-r)**2) - r*w**2

# A function that uses the secant method to find the root of a function
# fn to an accuracy tol given intial points in inital. 
def secant(initial,fn,tol):
	x1,x2 = initial
	i = 0 # start iteration counter
	while True:
		# Find slope of secant line connecting x1 and x2
		fprime = (f(x2) - f(x1))/(x2-x1) 
		# Find where current secant intersects the x-axIs
		x3 = x2 - fn(x2)*(1./fprime)
		# If accuracy not achieved, update x1 and x2 and try again
		if abs(x3 - x2) > tol:
			x1 = x2
			x2 = x3
			i+=1
		# If accuracy achieved, break the loop
		elif abs(x3 - x2) < tol:
			break
	return x3,i

# Two initial points
r1 = 10**8
r2 = 10**9
eps = 1e-6

# Call secant root finder
L1,itera = secant([r1,r2],f,eps)

print 'L1 = ',L1,'\tf(L1) = ',f(L1),'\nnumber of iterations: ',itera 
