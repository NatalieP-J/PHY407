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


# Choose the cut off for the Hamiltonian (since in reality its size is infinite)
mmaxs = [10,100]
nmaxs = mmaxs
evecs = []
for i in range(len(mmaxs)):
	mmax = mmaxs[i]
	nmax = nmaxs[i]
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
		evecs.append(evec)
	elif (H!= H.T).any() == True:
		print '''Matrix is not symmetric.
		         \n Cannot compute eigenvalues with numpy.linalg.eigvalsh'''

x = np.linspace(0,L,1000)
Nsamp = 50

states = []

for i in range(len(mmaxs)):
	states.append([])
	for k in range(3):
		estate = evecs[i][k]
		psi = wavefn(x,mmaxs[i],estate)
		A2 = gaussint(wavefn2,Nsamp,0,L,(mmaxs[i],estate))
		print A2
		#psi /= np.sqrt(A2)
		states[i].append(psi)

plt.subplot(311)
plt.xlim(0,5)
plt.title('Ground State')
plt.ylabel('$\psi_0(x)$',fontsize = 20)
for i in range(len(states)):
	plt.plot(x*1e10,states[i][0],label = 'nmax = mmax = {0}'.format(mmaxs[i]))
plt.subplot(312)
plt.xlim(0,5)
plt.title('First Excited State')
plt.ylabel('$\psi_1(x)$',fontsize = 20)
for i in range(len(states)):
	plt.plot(x*1e10,states[i][1],label = 'nmax = mmax = {0}'.format(mmaxs[i]))
plt.subplot(313)
plt.xlim(0,5)
plt.title('Second Excited State')
plt.ylabel('$\psi_2(x)$',fontsize = 20)
plt.xlabel('x [Angstroms]')
for i in range(len(states)):
	plt.plot(x*1e10,states[i][2],label = 'nmax = mmax = {0}'.format(mmaxs[i]))
#plt.tight_layout()
plt.show()

