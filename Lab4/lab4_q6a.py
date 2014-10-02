import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

# This code plots effeciency of an incadesent light bulb as a function of 
# temperature.

# Set constants for the program
# Planck's constant
h = 6.626 * 1e-34 #m^2 kg s^-1
# Speed of light
c = 3.000 * 1e8 #m s^-1
# Boltzmann constant
kB = 1.381 * 1e-23 #m^2 kg s^-1 K^-1
# Lower wavelength limit of visible light
wv1 = 390 * 1e-9 #m
# Upper wavelength limit of visible light
wv2 = 750 * 1e-9 #m

# Define a function to hold integrand of equation for eta
def etaint(x):
    return x**3/(np.exp(x) - 1)

# Define a function that will calculate eta, given a temperature T,
# a set of Gaussian quadrature points xs and weights ws
def eta(T,args):
    xs,ws = args
    a = h*c/(wv2*kB*T) # lower limit
    b = h*c/(wv1*kB*T) # upper limit
    x = 0.5*(b-a)*xs + 0.5*(b+a) # scale points
    w = 0.5*(b-a)*ws # scale weights
    eta = 0 # start integration sum 
    for n in range(Nsamp):
        eta += w[n]*etaint(x[n])
    eta *= (15./np.pi**4)
    return eta

# Choose number of sample points for Gaussian quadrature
Nsamp = 100

# Import Gaussian weights and points for an interval from -1 to 1
xs,ws = gaussxw(Nsamp)

# Create temperature array
T = np.arange(300,10000) # K

# Create empty array to hold resulting etas
etas = []

# Calculate eta for each T value
for i in range(len(T)):
    print 'Temperature rising ...',T[i],'K'
    etacal = eta(T[i],(xs,ws)) 
    etas.append(etacal)

# Plot eta vs T
plt.title('Efficiency of an incandescent bulb')
plt.ylabel('$\eta$',fontsize = 20)
plt.xlabel('$T$',fontsize = 20)
plt.plot(T,etas)
plt.show()
