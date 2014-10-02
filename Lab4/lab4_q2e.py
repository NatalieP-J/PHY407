import numpy as np
from numpy.linalg import eigh,eigvalsh
import matplotlib.pyplot as plt
from gaussint import gaussint

# This code computes the probability density of the first three eigenstates
# of a Hamiltonian describing a 1D infinite asymmetric quantum well with V(x) = a(x/L)

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
	# not allowed values for n,m
	if int(n) == 0 or int(m) == 0: 
		return 'invalid index 0'
	# if m and n are equal
	elif int(n) == int(m):
		return 0.5*a + (1./eV)*((np.pi*hbar*m)**2/(2*M*L**2))
	# if m and n are both even or both odd
	elif np.mod(int(n),2) != 0 and np.mod(int(m),2) != 0 or np.mod(int(n),2) == 0 and np.mod(int(m),2) == 0:
		return 0
	# if m or n is even and the other is odd
	elif np.mod(int(n),2) != 0 and np.mod(int(m),2) == 0 or np.mod(int(n),2) == 0 and np.mod(int(m),2) != 0:
		return -(8*a*n*m)/(np.pi*(m**2 - n**2))**2

# A function to compute the probability density of a particular state
# for a given set of Fourier coefficients.
def wavefn2(x,args):
	n,evec = args # Fourier coefficients
	# Depending on whether x is a single value or an array initialize psi
	# as an array or a float
	if isinstance(x,(list,np.ndarray))==True:
		psi = np.zeros(len(x))
	if isinstance(x,(float,int)):
		psi = 0
	# Construct the Fourier series
	for i in range(n):
		psi += evec[i]*np.sin(np.pi*(i+1)*x/L)
	# Return the square of the wave function
	return abs(psi)**2

# Choose number of terms in Fourier series to compute psi
mmax = 100
nmax = mmax
# Create placeholder matrix for H
H = np.zeros((mmax,nmax))

# Fill in values for H according to Hmn
# n,m in equations are algebraic indices and as such are one higher than Python indices
for m in range(mmax):
	for n in range(nmax):
		H[m,n] = Hmn(m+1.,n+1.)

# Confirm H is symmetric and find its eigenvalues and eigenvectors
if (H == H.T).all() == True:
	E = eigh(H)
	evec = E[1]
	evecs = evec.T # Transpose so ROWS in array are eigenvectors
elif (H!= H.T).any() == True:
	print '''Matrix is not symmetric.
	         \n Cannot compute eigenvalues with numpy.linalg.eigvalsh'''

# Create x array to span well
x = np.linspace(0,L,1000)
# Choose number of integration points for integral to normalize psi
Nsamp = 50

# Create list to hold the probablity density information
probden = []

# Find the first three probability density functions
# (ground, first excited and second excited states).
for k in range(3):
	psi_n = evecs[k] # Isolate Fourier coefficients for given state
	psi2 = wavefn2(x,(mmax,psi_n)) # Compute the probability density function for x
	A2 = gaussint(wavefn2,Nsamp,0,L,(mmax,psi_n)) # Compute normalization 
	psi2 /= A2 # Normalize probability function
	probden.append(psi2)

# Plot the probability of each state across the well's width
plt.xlim(0,5e-10)
plt.plot(x,probden[0],label = 'Ground State')
plt.plot(x,probden[1],label = 'First Excited State')
plt.plot(x,probden[2],label = 'Second Excited State')
plt.ylabel('$|\psi(x)|^2$',fontsize = 20)
plt.xlabel('$x\,[m]$',fontsize = 20)
plt.title('Probability Density for Asymmetric Quantum Well')
plt.legend(loc = 'best')
plt.show()

