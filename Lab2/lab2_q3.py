# This code computes the error in using the trapezoidal rule for integrals.
# This is done by computing the integral of a given function for 10 and 20 
# subdivisions and finding the error from the results.

# Function over which we will integrate
def f(x):
    return x**4 - 2*x + 1

# Set of two different choices for number of subdivision
Ns = [10,20]
# Lower bound of integral
a = 0.0
# Upper bound of integral
b = 2.0
# Empty list to hold the output of the integral calculations
Is = []

# Loop over different choices for number of subdivisions
for N in Ns: 
	# Width of a subdivision
	h = (b-a)/N
	# Begin calculating sum s
	s = 0.5*f(a) + 0.5*f(b)
	for k in range(1,N):
		s += f(a+k*h)
	# Add final result to list of results
	Is.append(h*s)

# Calculate the error 
eps = (1./3)*(Is[1]-Is[0])