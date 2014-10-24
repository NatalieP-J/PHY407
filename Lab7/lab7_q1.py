import cmath as cm
import numpy as np
import matplotlib.pyplot as plt

lam = np.arange(-20,5,0.1)
hk = np.arange(0.001,10,0.01)
hk /= 2.
#lams = np.zeros((len(lam),len(lam)),complex)

#for i in range(len(lams)):
#	for j in range(len(lams[i])):
#		lams[i][j] = lam[i] + lam[j]*1j


mu = np.zeros((len(lam),len(hk)),complex)

for i in range(len(mu)):
	for j in range(len(mu[i])):
		mu[i][j] = lam[i]*hk[j]


gf = (1+mu)/(1-mu)

fig, ax = plt.subplots(figsize = (8,8))
cax = ax.imshow(abs(gf),vmin = 0,vmax = 1,extent = [min(lam),max(lam),min(hk),max(hk)],aspect = 'auto')
plt.xlabel('$\lambda$',fontsize = 20)
plt.ylabel('$h_k$',fontsize = 20)
fig.colorbar(cax)
plt.title('Stability of the Implicit Trapezoid Method for $dy/dt = \lambda y$')