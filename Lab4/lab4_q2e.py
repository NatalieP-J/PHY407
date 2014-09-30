import numpy as np
from numpy.linalg import eigh,eigvalsh
import matplotlib.pyplot as plt
from gaussint import gaussint

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

def wavefn(x,n,evec):
	if isinstance(x,(list,np.ndarray))==True:
		psi = np.zeros(len(x))
	if isinstance(x,(float,int)):
		psi = 0
	for i in range(len(evec)):
		psi += evec[i]*np.sin(np.pi*(i+1)*x/L)
	return psi

def wavefn2(x,args):
	n,evec = args
	if isinstance(x,(list,np.ndarray))==True:
		psi = np.zeros(len(x))
	if isinstance(x,(float,int)):
		psi = 0
	for i in range(len(evec)):
		psi += evec[i]*np.sin(np.pi*(i+1)*x/L)
	return abs(psi)**2



mmax = 100
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
	E = eigh(H)
	evec = E[1]
	evecs = evec.T
elif (H!= H.T).any() == True:
	print '''Matrix is not symmetric.
	         \n Cannot compute eigenvalues with numpy.linalg.eigvalsh'''

x = np.linspace(0,L,1000)
Nsamp = 50

states = []

for k in range(3):
	psi_n = evecs[k]
	psi = wavefn2(x,(mmax,psi_n))
	A2 = gaussint(wavefn2,Nsamp,0,L,(mmax,psi_n))
	print A2
	psi /= np.sqrt(A2)
	states.append(psi)

plt.xlim(0,5)
plt.plot(x*1e10,states[0],label = 'Ground State')
plt.plot(x*1e10,states[1],label = 'First Excited State')
plt.plot(x*1e10,states[2],label = 'Second Excited State')
plt.ylabel('$|\psi(x)|^2$',fontsize = 20)
plt.xlabel('$x$',fontsize = 20)
plt.title('Probability Density for Asymmetric Quantum Well')
plt.legend(loc = 'best')
plt.show()

