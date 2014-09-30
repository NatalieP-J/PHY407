import numpy as np
import matplotlib.pyplot as plt

# This code solves a nonlinear function f(x) using over relaxation and
# counts the number of iterations

# Define nonlinear fuction 

def f(x,c):
	return 1-np.exp(-c*x)

# Set an array of constants for f(x)
cs = np.arange(0,3,0.01)
# Set initial guess
x0 = 1
# Set tolerance for result
eps = 1e-6

# Create empty list to hold the solutions
xs = []
# Iterate through each c value
for c in cs:
	# Reset xi to the initial guess
	xi = x0
	while True:
		xf = f(xi,c)
		# if tolerance is not achieved iterate again
		if abs(xf-xi) > eps:
			xi = xf
		#if tolerance achieved, stop loop
		elif abs(xf-xi) < eps:
			break
	xs.append(xf)

# Plot x vs c
plt.title('$Solutions\,to\,x=1-e^{-cx}\,for\,varying\,c$',fontsize = 20)
plt.xlabel('c')
plt.ylabel('x')
plt.plot(cs,xs)
plt.ylim(-0.1,1.0)
plt.show()