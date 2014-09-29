import numpy as np
from numpy.linalg import eigh,eigvalsh

# This code computes the energy eigenvalues of a Hamiltonian with matrix
# elements given by Hmn. This Hamiltonian describes a 1D infinite asymmetric
# quantum well with V(x) = a(x/L)

# Width of the well
L = 5*1e-10 #m
# Constant in potential equation
a = 10 #eV
# Mass of the electron
M = 9.1094*(1e-31) #kg
# Planck's constant
hbar = 1.0545*(1e-34) #J/s
# Electron volts per Joule
eV = 1.6022*(1e-19) #J

# A function to return the matrix elements of the Hamiltonian
def Hmn(m,n):
	if n == 0 or m == 0:
		return 'invalid index 0'
	elif n == m:
		return 0.5*a + (1./eV)*((np.pi*hbar*m)**2/(2*M*L**2))
	elif np.mod(n,2) != 0 and np.mod(m,2) != 0:
		return 0
	elif np.mod(n,2) == 0 and np.mod(m,2) == 0:
		return 0
	elif np.mod(n,2) != 0 and np.mod(m,2) == 0:
		return -(8*a*n*m)/(np.pi*(m**2 - n**2))**2
	elif np.mod(n,2) == 0 and np.mod(m,2) != 0:
		return -(8*a*n*m)/(np.pi*(m**2 - n**2))**2

# Choose the cut off for the Hamiltonian (since in reality its size is infinite)
mmax = 10
nmax = mmax

# Create placeholder matrix for H
H = np.zeros((mmax,nmax))

# Fill in values for H according to Hmn
# n,m in equations are algebraic indices and as such are one higher than Python indices
for m in range(mmax):
	for n in range(nmax):
		H[m,n] = Hmn(m+1,n+1)

# Confirm H is symmetric and find its eigenvalues
if (H == H.T).all() == True:
	E = eigvalsh(H)
	print E
elif (H!= H.T).any() == True:
	print '''Matrix is not symmetric.
		     \n Cannot compute eigenvalues with numpy.linalg.eigvalsh'''