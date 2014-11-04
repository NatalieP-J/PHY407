import numpy as np
import matplotlib.pyplot as plt
from dcst import dst,idst
plt.ion() # This line needed to run the animation


###############################################################################

# This code solves the one dimensional time-dependent Schrodinger equation for
# a box with rigid walls using the spectral method for solving PDEs.

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
# Float comparer
eps = 5e-19

################################## MAIN PROGRAM ##################################

# PDE SOLVER SPECIFICATIONS

# Number of position intervals
Nx = 1000
# Number of time intervals
Nt = 2000
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

# CREATE ARRAY OF INDICES FOR THE FOURIER SUM

k = np.arange(0,len(alpha))

# COMPUTE THE FACTOR MULTIPLIED IN THE ARGUMENTS OF THE FOURIER COEFFICIENTS

arg = -(hbar/(2*m))*(np.pi*k/L)**2

# BEGIN ANIMATION

fig = plt.figure()
ax = plt.axes()
line = ax.plot(x,psi.real)
ax.set_xlabel('$x [m]$',fontsize = 20)
ax.set_ylabel('$\psi$',fontsize = 20)

# BEGIN COMPUTING PSI AND ANIMATING THE RESULT 

psi_saves = [] # Array to hold snapshots

t = 0
while t < h*Nt:
    line[0].set_ydata(psi.real)
    ax.set_title('Time = {0} s'.format(t))
    plt.draw()
    alphan = alpha * np.cos(arg*t) # Compute one set of sine series coefficients
    etan = eta * np.sin(arg*t) # Compute the other set of S.S coefficients
    psi = idst(alphan) - idst(etan) # Perform an inverse discrete sine transformation
    psi[0] = psi0 # Impose boundary conditions
    psi[-1] = psi1
    if t < eps or abs(t-1e-16) < eps or abs(t-1e-15) < eps:
    	psi_saves.append(psi)
    t+=h


plt.figure()
plt.subplot(311)
plt.plot(x,psi_saves[0].real)
plt.ylabel('$\psi$',fontsize = 20)
plt.title('$0$ s')
plt.subplot(312)
plt.plot(x,psi_saves[1].real)
plt.ylabel('$\psi$',fontsize = 20)
plt.title('$10 ^{-16}$ s')
plt.subplot(313)
plt.plot(x,psi_saves[2].real)
plt.ylabel('$\psi$',fontsize = 20)
plt.xlabel('$x [m]$',fontsize = 20)
plt.title('$10 ^{-15}$ s')
plt.suptitle('Wave packet evolution over time',fontsize = 20)
plt.tight_layout()

