import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #m/s^2
A = 0.002 # whatever units eta (called n in code) has
mu = 0.5 #m
sig = 0.05 #m
xmin = 0.0 #m
xmax = 1.0 #m
J = 50 # number of position intervals
xdel = (xmax-xmin)/J #m
x = np.arange(xmin,xmax,xdel)
xhalf = np.arange(xmin+xdel/2.,xmax-xdel/2.,xdel)
tdel = 0.01 #s
tstart = 0.0 #s
tend = 400*tdel #s

def H(x):
	if isinstance(x,(np.ndarray,list)) == True:
		return np.array([0.01]*len(x))
	elif isinstance(x,(float,int)) == True:
		return 0.01
	else:
		print 'x value not float, int or array in H(x), no return'

def F(u,n,Hval):
	return g*n + (u**2)/2, u*(n+Hval)

uinit = 0
ninit = A*np.exp((-(x-mu)**2/(sig)**2))

u0 = 0
u1 = 0

uold = np.zeros(x.shape) + uinit
nold = np.zeros(x.shape) + ninit
uhalf = np.zeros(xhalf.shape)
nhalf = np.zeros(xhalf.shape)
unew = np.zeros(x.shape)
nnew = np.zeros(x.shape)
Hvals = H(x)
Hhalf = H(xhalf)

t = tstart

defac = tdel/(2*xdel)

J -= 1 #convert to python indices
while t < tend:
	Fvals = F(uold,nold,Hvals)
	for j in range(0,J):
		Fj1 = np.array([Fvals[0][j+1],Fvals[1][j+1]])
		Fj = np.array([Fvals[0][j],Fvals[1][j+1]])
		uhalf[j] = 0.5*(uold[j+1] + uold[j]) - defac*(Fj1[0] - Fj[0])
		nhalf[j] = 0.5*(nold[j+1] + nold[j]) - defac*(Fj1[1] - Fj[1])
	Fhalf = F(uhalf,nhalf,Hhalf)
	for j in range(1,J):
		Fj1 = np.array([Fhalf[0][j],Fhalf[1][j]])
		Fj = np.array([Fhalf[0][j-1],Fhalf[1][j-1]])
		unew[j] = uold[j] - 2*defac*(Fj1[0] - Fj[0])
		nnew[j] = nold[j] - 2*defac*(Fj1[1] - Fj[1])
	unew[0] = u0
	unew[J] = u1
	nnew[0] = nold[0] - 4*defac*(Fhalf[1][0] - Fvals[1][0])
	nnew[J] = nold[J] - 4*defac*(Fvals[0][J] - Fhalf[0][J-1])
	uold = np.copy(unew)
	nold = np.copy(nnew)
	t += tdel




