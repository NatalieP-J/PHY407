import numpy as np
from random import random,seed
from numpy.linalg import norm
import matplotlib.pyplot as plt

def f(r):
	return (r**-0.5)/(np.exp(r) + 1)


seed(7)

a = 0
b = 1

favg = 0
f2avg = 0

npts = int(1e5)

iterr = 100

Is = []
errs = []
for k in range(iterr):
	print 'Iteration',k+1
	for i in range(npts):
		r = abs(a-b)*random()+a
		favg += f(r)
		f2avg += f(r)**2

	favg *= (1/float(npts))
	f2avg *= (1/float(npts))

	varf = f2avg - favg**2
	err = (b-a)*(varf/float(npts))**0.5

	I = (b-a)*favg
	Is.append(I)
	errs.append(err)

plt.figure()
plt.errorbar(np.arange(1,iterr+1),Is,xerr = None,yerr = errs,fmt = 'o')
plt.xlabel('Iteration')
plt.ylabel('Intergral Value')
plt.xlim(0,iterr+2)
plt.title('Value of intgeral via the Mean Value Monte Carlo')
plt.show()

