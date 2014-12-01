import math
from time import clock
from numpy import arange,array
import matplotlib.pyplot as plt

def factorial(x):
	if x==0:
		return 1
	elif x > 0 and isinstance(x,int)==True:
		return x*factorial(x-1)
	else:
		print 'integers only'

def timeit(fn,indep):
	start = clock()
	val = fn(indep)
	end = clock()
	return val, end-start

indeps = arange(1,1000,1)

mathslist = []
factslist = []
for i in indeps:
	try:
		facts = timeit(factorial,i)
		maths = timeit(math.factorial,i)
		factslist.append(facts[1])
		mathslist.append(maths[1])
		print '{0}!\t my function: {1} s \t math module: {2} s'.format(i,facts[1],maths[1])
	except RuntimeError as edetails:
		print 'RuntimeError: ',edetails
		maths = timeit(math.factorial,i)
		mathslist.append(maths[1])
		print'{0}!\t my function: failed \t math module: {1} s'.format(i,maths[1])
