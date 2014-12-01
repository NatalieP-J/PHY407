import math
from time import clock

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

indeps = [10,100,500,1000]

for i in indeps:
	try:
		facts = timeit(factorial,i)
		maths = timeit(math.factorial,i)
		print '{0}!\t my function: {1} s \t math module: {2} s'.format(i,facts[1],maths[1])
	except RuntimeError as edetails:
		print 'RuntimeError: ',edetails
		maths = timeit(math.factorial,i)
		print'{0}!\t my function: failed \t math module: {1} s'.format(i,maths[1])