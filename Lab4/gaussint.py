from gaussxw import gaussxwab

# A function to compute an integral using Gaussian quadrature
# This function relies on gaussxwab from gaussxw.py
def gaussint(fn,Nsamp,lowlim,uplim,args = False):
	"""
	Returns the integral of fn from lowlim to uplim using Gaussian 
	quadrature with Nsamp sample points.

	"""
	x,w = gaussxwab(Nsamp,lowlim,uplim) # gets points and weights
	print x,w
	s = 0.0 # start sum at zero
	for i in range(Nsamp):
		if args == False:
			s += w[i]*fn(x[i]) # evaluate fn at points and weight it
		elif args != False:
			s += w[i]*fn(x[i],args) # evaluate fn at points and weight it
	return s