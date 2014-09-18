from math import exp
import numpy as np
import time
import matplotlib.pyplot as plt

exps = np.arange(3,7)
termslist = 10**exps
times = np.array([])
for term in termslist:
    terms = term
    beta = 1./100.
    S = 0.0
    Z = 0.0
    start = time.clock()
    for n in range(terms):
        E = n + 0.5
        weight = exp(-beta*E)
        S += weight*E
        Z += weight
    end = time.clock()
    times = np.append(times,end-start)

plt.xlabel('Number of terms in sum')
plt.ylabel('Time [s]')
plt.title('Time to compute a sum with a given number of terms')
plt.loglog(termslist,times,'o')
plt.xlim(10**2.5,10**6.18)
plt.show()

flops = 7 
flopslist = flops*termslist
flopss = flopslist/times
ncores = 2.0
print 'My machine flops/second = 10^',np.log10(np.mean(flopss/ncores))
topsup = 3.3862699999999996e+16
ncores = 3120000.0
print 'June 2014 top supercomputer = 10^',np.log10((topsup/ncores))
