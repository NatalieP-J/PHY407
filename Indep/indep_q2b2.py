from scipy.special import jn,gamma
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from math import factorial
from gaussxw import gaussxwab
plt.ion()

###############################################################################

# This code uses the sum form of the Bessel functions to find J0

################################## CONSTANTS ##################################

# A list of the number of terms for each sum
kmaxs = [25,50,75]

################################## FUNCTIONS ##################################

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

# Returns the value of J0 at x using a sum with kmax terms
def J0sum(x,kmax):
	Jval = np.zeros(np.shape(x))
	for k in range(kmax):
		Jvaladd = (((-1.)**k)/(float(factorial(k))**2))*(x/2.)**(2*k)
		Jval += Jvaladd
	return Jval

################################## MAIN PROGRAM ##################################

# Create array in the independent variable
xmin = 0
xmax = 20
step = 0.01
x = np.arange(xmin,xmax+step,step)

# Create list to hold results of evaluating J0 with different number of terms
# in the sum
J0_sums = []
for i in range(len(kmaxs)):
	J0_sum = J0sum(x,kmaxs[i])
	J0_sums.append(J0_sum)
sci = jn(0,x)

################################## PLOT ##################################
plt.figure()
gs = gridspec.GridSpec(2, 1, height_ratios=[2.5, 1]) 
plt.subplot(gs[0])
for i in range(len(J0_sums)):
	plt.plot(x,J0_sums[i],label = '# terms in sum = {0}'.format(kmaxs[i]))
plt.plot(x,sci,label = 'Scipy module')
plt.legend(loc = 'best')
plt.ylabel('$J_0(x)$',fontsize = 20)
plt.xlim(xmin,xmax)
plt.ylim(-0.5,1.0)
plt.title('Bessel function $J_0$ with Equation 4',fontsize = 20)
plt.subplot(gs[1])
for i in range(len(J0_sums)):
	plt.plot(x,abs(J0_sums[i]-sci),label = '# terms in sum = {0}'.format(kmaxs[i]))
plt.ylabel('Residuals')
plt.xlabel('x')
plt.xlim(xmin,xmax)
plt.ylim(0,0.5)
plt.show()
