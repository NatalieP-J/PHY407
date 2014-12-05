import math
from time import clock

factlist = {}

def factorial(x):
	if x==0:
		factlist[0] = 1
		return 1
	elif x in factlist.keys():
		return factlist[x]
	elif x not in factlist.keys() and isinstance(x,int) == True:
		factlist[x] = x*factorial(x-1)
		return factlist[x]
	else:
		print 'integers only'

def timeit(fn,indep):
	start = clock()
	val = fn(indep)
	end = clock()
	return val, end-start

indeps = [1000,10,10,100,100,500,500,1000,1000]

for i in indeps:
	try:
		facts = timeit(factorial,i)
		maths = timeit(math.factorial,i)
		print '{0}!\t my function: {1} s \t math module: {2} s'.format(i,facts[1],maths[1])
	except RuntimeError as edetails:
		print 'RuntimeError: ',edetails
		maths = timeit(math.factorial,i)
		print'{0}!\t my function: failed \t math module: {1} s'.format(i,maths[1])