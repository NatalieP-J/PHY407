from __future__ import division
import math
from time import clock

###############################################################################

# This code compares various factorial functions with the built in function

################################## SAMPLE OUTPUT ##################################

'''
Part a)
1000!	 my function: exceeded recursion depth 	 math module: 0.000373999999993657 s
10!	 my function: 1.49999999905504e-05 s 	 math module: 1.99999999495049e-06 s residual %: 0.0
10!	 my function: 2.60000000196214e-05 s 	 math module: 5.00000001579792e-06 s residual %: 0.0
100!	 my function: 0.000154999999978145 s 	 math module: 1.59999999880256e-05 s residual %: 0.0
100!	 my function: 0.000188000000008515 s 	 math module: 8.99999997727718e-06 s residual %: 0.0
500!	 my function: 0.000412000000011403 s 	 math module: 0.000188000000008515 s residual %: 0.0
500!	 my function: 0.000855000000001382 s 	 math module: 0.000151999999985719 s residual %: 0.0
1000!	 my function: exceeded recursion depth 	 math module: 0.000454999999988104 s
1000!	 my function: exceeded recursion depth 	 math module: 0.000548000000009097 s
Part b)
1000!	 my function: overflowed the exp 	 math module: 0.000381000000004406 s
10!	 my function: 5.00000001579792e-06 s 	 math module: 1.99999999495049e-06 s residual %: 13.7612875249463
10!	 my function: 2.00000002337219e-06 s 	 math module: 9.99999997475243e-07 s residual %: 13.7612875249463
100!	 my function: 9.99999997475243e-07 s 	 math module: 1.59999999880256e-05 s residual %: 0.88589720368673
100!	 my function: 9.99999997475243e-07 s 	 math module: 1.00000000031741e-05 s residual %: 0.88589720368673
500!	 my function: overflowed the exp 	 math module: 0.000172999999989543 s
500!	 my function: overflowed the exp 	 math module: 0.000141999999982545 s
1000!	 my function: overflowed the exp 	 math module: 0.000465999999988753 s
1000!	 my function: overflowed the exp 	 math module: 0.000374999999991132 s
Part c)
1000!	 my function: exceeded recursion depth 	 math module: 0.000551000000001522 s
10!	 my function: 1.89999999804513e-05 s 	 math module: 1.99999999495049e-06 s residual %: 0.0
10!	 my function: 5.00000001579792e-06 s 	 math module: 2.00000000063483e-05 s residual %: 0.0
100!	 my function: 0.000180999999997766 s 	 math module: 1.00000000031741e-05 s residual %: 0.0
100!	 my function: 5.99999998485146e-06 s 	 math module: 9.00000000569889e-06 s residual %: 0.0
500!	 my function: 0.00262599999999225 s 	 math module: 0.000194000000021788 s residual %: 0.0
500!	 my function: 3.59999999943739e-05 s 	 math module: 0.000166000000007216 s residual %: 0.0
1000!	 my function: 0.0158119999999826 s 	 math module: 0.000562999999999647 s residual %: 0.0
1000!	 my function: 4.10000000101718e-05 s 	 math module: 0.000629000000003543 s residual %: 0.0
'''


################################## FUNCTIONS ##################################

# A function that times the evaluation of a function fn
def timeit(fn,indep):
	start = clock()
	val = fn(indep)
	end = clock()
	return val, end-start

# Basic recursive factorial function
def factorial_a(x):
	if x==0:
		return 1
	elif x > 0 and isinstance(x,int)==True:
		return x*factorial_a(x-1)
	else:
		print 'integers only'

# Stirling's approximation
def factorial_b(x):
	return math.exp(x*math.log(x)-x)

# An empty dictionary for use by factorial_c
factlist = {}

# A recursive factorial function that uses memoization
def factorial_c(x):
	if x==0:
		factlist[0] = 1
		return 1
	elif x in factlist.keys():
		return factlist[x]
	elif x not in factlist.keys() and isinstance(x,int) == True:
		factlist[x] = x*factorial_c(x-1)
		return factlist[x]
	else:
		print 'integers only'

################################## MAIN PROGRAM ##################################

# Factorials to evaluate
indeps = [1000,10,10,100,100,500,500,1000,1000]

# Compare factorial_a to math.factorial
print 'Part a)'
for i in indeps:
	try:
		facts = timeit(factorial_a,i)
		maths = timeit(math.factorial,i)
		# Compute the percentage of the factorial value that the residual makes up
		resfrac = (abs(facts[0]-maths[0])/maths[0])*100
		print '{0}!\t my function: {1:.15} s \t math module: {2:.15} s \t residual %: {3}'.format(i,facts[1],maths[1],resfrac)
	except RuntimeError as edetails:
		maths = timeit(math.factorial,i)
		print'{0}!\t my function: exceeded recursion depth \t math module: {1:.15} s'.format(i,maths[1])

# Compare factorial_b to math.factorial
print 'Part b)'
for i in indeps:
	try:
		facts = timeit(factorial_b,i)
		maths = timeit(math.factorial,i)
		# Compute the percentage of the factorial value that the residual makes up
		resfrac = (abs(math.log(facts[0])-math.log(maths[0]))/math.log(maths[0]))*100
		print '{0}!\t my function: {1:.15} s \t math module: {2:.15} s \t residual % (in exp): {3:.15}'.format(i,facts[1],maths[1],resfrac)
	except OverflowError as edetails:
		maths = timeit(math.factorial,i)
		print'{0}!\t my function: overflowed the exp \t math module: {1:.15} s'.format(i,maths[1])

# Compare factorial_c to math.factorial
print 'Part c)'
for i in indeps:
	try:
		facts = timeit(factorial_c,i)
		maths = timeit(math.factorial,i)
		# Compute the percentage of the factorial value that the residual makes up
		resfrac = (abs(facts[0]-maths[0])/maths[0])*100
		print '{0}!\t my function: {1:.15} s \t math module: {2:.15} s \t residual %: {3}'.format(i,facts[1],maths[1],resfrac)
	except RuntimeError as edetails:
		maths = timeit(math.factorial,i)
		print'{0}!\t my function: exceeded recursion depth \t math module: {1:.15} s'.format(i,maths[1])


