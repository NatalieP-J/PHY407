# This code uses Simpson's rule to calculate the integral of 
# x^4 - 2x + 1 from 0 to 2

# Define function we wish to calculate an integral for
def f(x):
    return x**4 - 2*x + 1

# Number of subdivisions of the interval
N = 10
# Lower bound
a = 0.0
# Upper bound
b = 2.0
# Width of each subdivision
h = (b-a)/N

# Start the sum, called s
s = (1./3)*f(a) + (1./3)*f(b)
# Sum over odd k
for k in range(1,N,2):
    s += (4./3)*f(a+k*h)
# Sum over even k
for k in range(2,N-1,2):
	s += (2./3)*f(a+k*h)

#compute the final result of the integral
i = h*s
# Print final result of integral
print i