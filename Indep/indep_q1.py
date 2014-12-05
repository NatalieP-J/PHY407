from __future__ import division
import math
from time import clock

###############################################################################

# This code compares various factorial functions with the built in function

################################## SAMPLE OUTPUT ##################################

'''
Part a)
1000!	 my function: exceeded recursion depth 	 math module: 0.000672999999977719 s
10!	 my function: 1.80000000113978e-05 s 	 math module: 2.00000002337219e-06 s 	 residual %: 0.0
10!	 my function: 2.2999999998774e-05 s 	 math module: 6.00000001327317e-06 s 	 residual %: 0.0
100!	 my function: 0.000188000000008515 s 	 math module: 1.79999999829761e-05 s 	 residual %: 0.0
100!	 my function: 8.30000000178188e-05 s 	 math module: 2.00000000063483e-05 s 	 residual %: 0.0
500!	 my function: 0.000942000000009102 s 	 math module: 0.000228999999990265 s 	 residual %: 0.0
500!	 my function: 0.000638000000009242 s 	 math module: 0.000212000000004764 s 	 residual %: 0.0
1000!	 my function: exceeded recursion depth 	 math module: 0.000578000000018619 s
1000!	 my function: exceeded recursion depth 	 math module: 0.000564000000025544 s
Part b)
1000!	 my function: overflowed the exp 	 math module: 0.000615000000010468 s
10!	 my function: 1.10000000006494e-05 s 	 math module: 1.99999999495049e-06 s 	 residual %: 0.000220264657948066
10!	 my function: 3.99999998990097e-06 s 	 math module: 1.99999999495049e-06 s 	 residual %: 0.000220264657948066
100!	 my function: 6.9999999823267e-06 s 	 math module: 1.59999999880256e-05 s 	 residual %: 2.68811714181602e-155
100!	 my function: 2.99999999242573e-06 s 	 math module: 1.59999999880256e-05 s 	 residual %: 2.68811714181602e-155
500!	 my function: overflowed the exp 	 math module: 0.000205999999991491 s
500!	 my function: overflowed the exp 	 math module: 0.000182999999992717 s
1000!	 my function: overflowed the exp 	 math module: 0.000529000000000224 s
1000!	 my function: overflowed the exp 	 math module: 0.000578000000018619 s
Part c)
1000!	 my function: exceeded recursion depth 	 math module: 0.000366000000013855 s
10!	 my function: 1.19999999981246e-05 s 	 math module: 1.99999999495049e-06 s 	 residual %: 0.0
10!	 my function: 1.99999999495049e-06 s 	 math module: 9.99999997475243e-07 s 	 residual %: 0.0
100!	 my function: 0.000191999999998416 s 	 math module: 1.59999999880256e-05 s 	 residual %: 0.0
100!	 my function: 5.99999998485146e-06 s 	 math module: 1.29999999955999e-05 s 	 residual %: 0.0
500!	 my function: 0.00378200000000106 s 	 math module: 0.000180999999997766 s 	 residual %: 0.0
500!	 my function: 2.2999999998774e-05 s 	 math module: 0.000131999999979371 s 	 residual %: 0.0
1000!	 my function: 0.0198450000000037 s 	 math module: 0.000607000000002245 s 	 residual %: 0.0
1000!	 my function: 4.30000000051223e-05 s 	 math module: 0.000373999999993657 s 	 residual %: 0.0
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
		resfrac = (math.exp(abs(math.log(facts[0])-math.log(maths[0])))/float(maths[0]))*100
		print '{0}!\t my function: {1:.15} s \t math module: {2:.15} s \t residual %: {3:.15}'.format(i,facts[1],maths[1],resfrac)
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


