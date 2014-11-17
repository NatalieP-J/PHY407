import numpy as np
from random import random,seed
from numpy.linalg import norm
import matplotlib.pyplot as plt

def fw(r):
	return 1./(np.exp(r) + 1)


seed(7)

a = 0
b = 1

fwavg = 0
fw2avg = 0

wint = 2.

npts = int(1e5)

iterr = 100

Is = []
errs = []
for k in range(iterr):
	print 'Iteration',k+1
	for i in range(npts):
		r = (abs(a-b)*random()+a)**2
		fwavg += fw(r)
		fw2avg += (fw(r))**2

	fwavg *= (1/float(npts))
	fw2avg *= (1/float(npts))
	varfw = fw2avg - fwavg**2

	err = wint*(varfw/float(npts))**0.5

	I = wint*fwavg
	Is.append(I)
	errs.append(err)

plt.figure()
plt.errorbar(np.arange(1,iterr+1),Is,xerr = None,yerr = errs,fmt = 'o')
plt.xlabel('Iteration')
plt.ylabel('Intergral Value')
plt.xlim(0,iterr+2)
plt.title('Value of intgeral via the Importance Sampling Monte Carlo')
plt.show()

plt.figure()
plt.hist(Is,10,range = [0.8,0.88])
plt.plot()
plt.show()
