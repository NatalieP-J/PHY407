import math
from time import clock
import matplotlib.pyplot as plt
from matplotlib import gridspec
from numpy import array

def factorial(x):
	return math.exp(x*math.log(x)-x)

def lnfactorial(x):
	return x*math.log(x) - x

def lnmath(x):
	return math.log(math.factorial(x))

def timeit(fn,indep):
	start = clock()
	val = fn(indep)
	end = clock()
	return val, end-start

indeps = [10,100,500,1000]

for i in indeps:
	try:
		facts = timeit(factorial,i)
		maths = timeit(math.factorial,i)
		print '{0}!\t my function: {1} s \t math module: {2} s'.format(i,facts[1],maths[1])
	except OverflowError as edetails:
		print 'OverflowError: ',edetails
		maths = timeit(math.factorial,i)
		print'{0}!\t my function: failed \t math module: {1} s'.format(i,maths[1])

indep = range(1,1001)
maths  = []
facts = []

for i in indep:
	maths.append(lnmath(i))
	facts.append(lnfactorial(i))

plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[2.5, 1]) 
plt.subplot(gs[0])
plt.plot(indep,maths)
plt.plot(indep,facts)
plt.ylabel('ln(n!)')
plt.subplot(gs[1])
plt.plot(indep, abs(array(maths)-array(facts)))
plt.xlabel('n')
plt.ylabel('Residual')
plt.show()
