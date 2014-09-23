from gaussint import gaussint
import numpy as np

# This program computes the integral of x^3/(exp(x) - 1) from zero 
# to infinity

# Set constants for program
# Number of sample points
N = 50
# Lower limit of integral
a = 0.
# Upper limit of integral
b = 1.
# Speed of light in a vacuum
c = 3.e8 #m/s
# Boltzmann constant
kb = 1.381e-23 #m^2 kg s^-2 K^-1
# Planck's constant
hbar = 1.055e-34 #m^2 kg s^-1
# Stefan-Boltzmann constant
sigtrue = 5.670373e-8 #W m^-2 K^-4

# Function returns z^3/(exp(z) - 1)dz under change of variables 
# z = x/(1-x). This makes the integration limits finite.
def Wintr(x):
	num = x**3 # numerator
	den = (1-x)**5 * (np.exp(x/(1-x))-1) # denominator
	return num/den

# Return evaluation of integral
Wintg = gaussint(Wintr,N,a,b)

sig = Wintg*kb**4/(4*(np.pi*c)**2*hbar**3)

print 'Stefan-Boltzmann constant:\n calculated: ', sig,'\t true: ',sigtrue