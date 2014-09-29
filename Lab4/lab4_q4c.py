import numpy as np

# This code solves a nonlinear function f(x) using over relaxation and
# counts the number of iterations

# Define nonlinear fuction 
def f(x,c):
	return 1-np.exp(-c*x)

# Set constant for function
c = 2
# Set initial guess
x0 = 1
# Set tolerance level for answer
eps = 1e-6
# Define omega for over relaxation
w = 0.5

xi = x0
# Start iteration counter
i = 0
while True:
	xf = (w+1)*f(xi,c) - w*xi
	# if tolerance is not achieved iterate again
	if abs(xf-xi) > eps:
		xi = xf
		i+=1
	# if tolerance achieved, stop loop
	elif abs(xf-xi) < eps:
		break

# Print number of iterations
print i,' iterations'