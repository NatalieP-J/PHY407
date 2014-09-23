from gaussxw import gaussxwab

# A function to compute an integral using Gaussian quadrature
# This function relies on gaussxwab from gaussxw.py
def gaussint(fn,Nsamp,lowlim,uplim):
	"""
	Returns the integral of fn from lowlim to uplim using Gaussian 
	quadrature with Nsamp sample points.

	"""
	x,w = gaussxwab(Nsamp,lowlim,uplim) # gets points and weights
	s = 0.0 # start sum at zero
	for i in range(Nsamp):
		s += w[i]*fn(x[i]) # evaluate fn at points and weight it
	return s