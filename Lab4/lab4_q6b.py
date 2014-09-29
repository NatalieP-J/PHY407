import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw

# This code plots effeciency of an incadesent light bulb as a function of 
# temperature.

# Set constants for the program
# Planck's constant
h = 6.62606957 * 1e-34 #m^2 kg s^-1
# Speed of light
c = 3.000 * 1e8 #m s^-1
# Boltzmann constant
kB = 1.3806488 * 1e-23 #m^2 kg s^-1 K^-1
# Lower wavelength limit of visible light
wv1 = 390 * 1e-9 #m
# Upper wavelength limit of visible light
wv2 = 750 * 1e-9 #m
# Golden ratio
z = 0.5 + np.sqrt(5)/2.

# Define a function to hold integrand of equation for eta
def etaint(x):
    return x**3/(np.exp(x) - 1)

def eta(T,xs,ws):
    a = h*c/(wv2*kB*T)
    b = h*c/(wv1*kB*T)
    x = 0.5*(b[i]-a[i])*xs + 0.5*(b[i]+a[i])
    w = 0.5*(b[i]-a[i])*ws
    eta = 0
    for n in range(Nsamp):
        eta += w[n]*etaint(x[n])
    eta *= (15./np.pi**4)
    return eta

def getx2(x1,x4):
    return x4 - (x4-x1)*(1./z)

def getx3(x1,x4):
    return x1 + (x4-x1)*(1./z)

# Choose number of sample points for Gaussian quadrature
Nsamp = 100

# Import Gaussian weights and points for an interval from -1 to 1
xs,ws = gaussxw(Nsamp)

eps = 1.

T1 = 6000
T4 = 8000
T2 = getx2(T1,T4)
T3 = getx3(T1,T4)

while True:
    

'''
# Set upper and lower limits for eta integral for each temperature
a = h*c/(wv2*kB*T)
b = h*c/(wv1*kB*T)

# Create empty array to hold resulting etas
etas = []

# Calculate eta for each T value
for i in range(len(T)):
    print 'Temperature rising ...',T[i],'K'
    # Scale weights and points for Gaussian quadrature appropriately
    x = 0.5*(b[i]-a[i])*xs + 0.5*(b[i]+a[i])
    w = 0.5*(b[i]-a[i])*ws
    # Calculate integral in eta with Gaussian quadrature
    eta = 0
    for n in range(Nsamp):
        eta += w[n]*etaint(x[n])
    # Multiply eta by leading factor
    eta *= (15./np.pi**4)
    etas.append(eta)

# Plot eta vs T
plt.title('Effiecieny of an incandescent bulb')
plt.ylabel('$\eta$',fontsize = 20)
plt.xlabel('$T$',fontsize = 20)
plt.plot(T,etas)
plt.show()
'''
