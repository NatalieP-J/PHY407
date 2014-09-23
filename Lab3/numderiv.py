def fdiff(f,x,h):
	return (f(x+h)-f(x))/h

def cdiff(f,x,h):
	return (f(x+0.5*h) - f(x-0.5*h))/h