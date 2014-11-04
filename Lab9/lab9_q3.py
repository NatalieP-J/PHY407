import numpy as np
import matplotlib.pyplot as plt
from dcst import dst,idst

###############################################################################

# This code finds the Fourier transform of a complex-valued function and plots 

################################## CONSTANTS ##################################

# Mass of the electron
m = 9.109e-31 #kg
# Planck's constant
hbar = 1.055e-34 #m^2 kg/s
# Size of box
L = 1e-8 #m
# Centre position of initial wave packet
x0 = L/2. #m
# Width of initial wave packet
sig = 1e-10 #m
# Frequency of initial wave packet
kap = 5e10 #m^-1

################################## MAIN PROGRAM ##################################

# PDE SOLVER SPECIFICATIONS

# Number of position intervals
Nx = 1000
# Number of time intervals
Nt = 500
# Position step size
a = float(L/Nx) #m
# Time step size
h = 1e-18 #s
# Position array
x = np.arange(0,L,a)

# INITIALIZE PSI ARRAY

psi = np.zeros(len(x),complex)

# SET BOUNDARY INITIAL CONDITIONS FOR PSI

psi0 = 0.
psi1 = 0.
psi_init = np.exp(-(x[1:len(x)-2] - x0)**2/(2*sig**2))*np.exp(1j*kap*x[1:len(x)-2])

# CREATE INITAL PSI ARRAY

psi[0] = psi0
psi[-1] = psi1
psi[1:len(x)-2] = psi_init

# DIVIDE INTO REAL AND IMAGINARY PARTS

psiR = psi.real
psiI = psi.imag

# PERFORM DISCRETE SINE TRANSFORMS

alpha = dst(psiR)
eta = dst(psiI)

################################## PLOT ##################################

plt.plot(np.abs(alpha + 1j*eta))
plt.ylabel('$|b_k|$',fontsize = 20)
plt.xlabel('$k$',fontsize = 20)
plt.title('Fourier Coefficients')
