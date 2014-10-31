import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #m/s^2
A = 0.0005 # whatever units eta (called n in code) has
mu = 0.0 #m
sig = 0.1 #m
xmin = 0.0 #m
xmax = 1.0 #m
J = 150 # number of position intervals
xdel = (xmax-xmin)/J #m
x = np.arange(xmin,xmax,xdel)
xhalf = np.arange(xmin+xdel/2.,xmax-xdel/2.,xdel)
tdel = 0.001 #s
tstart = 0.0 #s
tend = 4000*tdel #s

def H(x):
	if isinstance(x,(np.ndarray,list)) == True:
		H = np.zeros(x.shape)
		int1 = np.where((x >= 0)&(x < 0.25))
		H[int1] = 2.
		int2 = np.where((x >= 0.25) & (x < 0.75))
		H[int2] = 1-np.tanh(8*np.pi*(x[int2]-0.5))
		int3 = np.where((x >= 0.75) & (x <= 1.))
		H[int3] = 0.
		return 0.0005 + 0.01*H
	elif isinstance(x,(float,int)) == True:
		if x >= 0 and x < 0.25:
			return 0.0005 + 0.01*2.
		if x >= 0.25 and x < 0.75:
			return 0.0005 + 0.01*(1-np.tanh(8*np.pi*(x-0.5)))
		if x >= 0.75 and x <= 1.:
			return 0.0005 + 0.01*0

def F(u,n,Hval):
	return g*n + (u**2)/2, u*(n+Hval)

uinit = np.zeros(x.shape)
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
	nnew[0] = nold[0] - 2*defac*(Fhalf[1][0] - Fvals[1][0])
	nnew[J] = nold[J] - 2*defac*(Fvals[0][J] - Fhalf[0][J-1])
	#rprint unew,nnew
	uold = np.copy(unew)
	nold = np.copy(nnew)
	t += tdel




