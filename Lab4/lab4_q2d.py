import numpy as np
from numpy.linalg import eigh,eigvalsh
import matplotlib.pyplot as plt

L = 5*1e-10 #m
a = 10 #eV
M = 9.1094*(1e-31) #kg
hbar = 1.0545*(1e-34) #J/s
eV = 1.6022*(1e-19) #J

def Hmn(m,n):
	if int(n) == 0 or int(m) == 0:
		return 'invalid index 0'
	elif int(n) == int(m):
		return 0.5*a + (1./eV)*((np.pi*hbar*m)**2/(2*M*L**2))
	elif np.mod(int(n),2) != 0 and np.mod(int(m),2) != 0 or np.mod(int(n),2) == 0 and np.mod(int(m),2) == 0:
		return 0
	elif np.mod(int(n),2) != 0 and np.mod(int(m),2) == 0 or np.mod(int(n),2) == 0 and np.mod(int(m),2) != 0:
		return -(8*a*n*m)/(np.pi*(m**2 - n**2))**2

mmaxs = [10,100]
nmaxs = mmaxs

energies = []

for i in range(len(mmaxs)):
	mmax = mmaxs[i]
	nmax = nmaxs[i]

	H = np.zeros((mmax,nmax))

	for m in range(mmax):
		for n in range(nmax):
			H[m,n] = Hmn(m+1.,n+1.)

	E = eigvalsh(H)[:10]
	energies.append(E)

plt.title('Residuals in Energy Eigenvalue Calculations')
plt.xlabel('$Energies\, for\, H_{10\mathrm{x}10}$',fontsize = 18)
plt.ylabel('$Energies\, for\, H_{10\mathrm{x}10}\, - \,Energies\, for\, H_{100\mathrm{x}100}$',fontsize = 18)
plt.semilogy(energies[0],energies[0] - energies[1],'o')
plt.show()


Estr = ''

for i in range(10):
	Estr += '\n E_{0} & {1} & {2} & {3}\n\\hline'.format(i,energies[0][i],energies[1][i],energies[0][i] - energies[1][i])

print Estr