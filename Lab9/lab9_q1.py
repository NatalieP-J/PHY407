import numpy as np
import matplotlib.pyplot as plt
from banded import banded
import cmath as cm


###############################################################################

# This code solves the one dimensional time-dependent Schrodinger equation for
# a box with rigid walls using the Crank-Nicolson method for solving PDEs.

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

################################## FUNCTIONS ##################################

def vvec(psi):
    v = np.zeros(len(psi),complex)
    v[0] = b1*psi[0] + b2*psi[1]
    v[-1] = b1*psi[-1] + b2*psi[-2]
    for i in range(1,len(psi)-1):
        v[i] = b1*psi[i] + b2*(psi[i+1] + psi[i-1])
    return v

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

# MATRIX ELEMENTS FOR CRANK-NICOLSON METHOD

ele = h*(1j*hbar/(4*m*a**2))
a1 = 1 + 2*ele
a2 = -ele
b1 = 1 - 2*ele
b2 = ele

# INITIALIZE 'A' MATRIX, FORMATED FOR BANDED

A = np.zeros((3,len(x)),complex)

# UPDATE ELEMENTS OF 'A'

# Up-diagonal entries
A[0][2:] += a2
# Down-diagonal entries
A[2][:-2] += a2
# Diagonal entries
A[1][1:-1] += a1
# Choose first and last row to be corresponding rows of the identity 
# matrix so that boundary conditions remain as selected
A[1][0] += 1.0
A[1][-1] += 1.0

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


# BEGIN COMPUTING PSI

t = 0
while t < Nt*h:
    v = vvec(psi) # Create v vector
    psi = banded(A,v,1,1) # Use Gaussian elimination on banded matrices to update psi
    t+=h

