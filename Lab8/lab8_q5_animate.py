import numpy as np
import matplotlib.pyplot as plt
plt.ion()

###############################################################################

# This code solves the shallow water equations in 1 dimension with the Two-Step 
# Lax-Wendroff scheme and rigid wall boundary conditions.

################################## CONSTANTS ##################################

# Gravitational acceleration
g = 9.81 #m/s^2
# Amplitude of initial (Gaussian) wave
A = 0.002
# Initial centre postion of wave
mu = 0.5 #m
# FWHM of the wave
sig = 0.05 #m
# Lower x boundary
xmin = 0.0 #m
# Upper x boundary
xmax = 1.0 #m
# Number of position intervals
J = 50
# Position step size
xdel = (xmax-xmin)/J #m
# Position array
x = np.arange(xmin,xmax,xdel) #m
# Half step position array
xhalf = np.arange(xmin+xdel/2.,xmax-xdel/2.,xdel)
# Time step size
tdel = 0.01 #s
# Choose start time
tstart = 0.0 #s
# Choose end time
tend = 400*tdel #s
# Set times of interest
stimes = np.array([0.,1.,4.])
# Set small difference for float comparison
eps = tdel*(1e-2)

################################## FUNCTIONS ##################################

# Function that defines the bottom topography
def H(x):
	if isinstance(x,(np.ndarray,list)) == True:
		return np.array([0.01]*len(x))
	elif isinstance(x,(float,int)) == True:
		return 0.01

# Flux vector
def F(u,n,Hvals):
	return (g*n + (u**2)/2.),u*(n+Hvals)

################################## MAIN PROGRAM ##################################

# Here, u is represented with letter u, but eta is represented with letter n

# Set initial conditions
uinit = np.zeros(x.shape)
ninit = A*np.exp((-(x-mu)**2/(sig)**2))

# Set boundary conditions
u0 = 0 # at x = 0
u1 = 0 # at x = 1

# Initialize arrays - two to hold the initial values at each timestep,
# two to hold updated results after a timestep is completed
uold = np.zeros(x.shape) + uinit
nold = np.zeros(x.shape) + ninit
uhalf = np.zeros(xhalf.shape)
nhalf = np.zeros(xhalf.shape)
unew = np.zeros(x.shape)
nnew = np.zeros(x.shape)

# Calculate an array with the height of the bottom at each x position
Hvals = H(x)
Hhalf = H(xhalf)

# Set time to start time
t = tstart

# Calculate a prefactor to the flux term in the updating expressions
defac = tdel/(2*xdel)

J -= 1 #convert to python indices

savetimes = []

fig = plt.figure()
ax = plt.axes(xlim = (xmin,xmax), ylim = (-0.006,0.008))
line = ax.plot(x,ninit)
ax.set_xlabel('$x [m]$',fontsize = 20)
ax.set_ylabel('$\eta$',fontsize = 20)

while t < tend+2*tdel:
	Fu,Fn = F(uold,nold,Hvals) # Calculate the flux for u and eta
	for j in range(J): # For interior grid points use central difference
		uhalf[j] = 0.5*(uold[j+1] + uold[j]) - defac*(Fu[j+1] - Fu[j])
		nhalf[j] = 0.5*(nold[j+1] + nold[j]) - defac*(Fn[j+1] - Fn[j]) 
	Fuhalf,Fnhalf = F(uhalf,nhalf,Hhalf)
	for j in range(1,J):
		unew[j] = uold[j] - 2*defac*(Fuhalf[j] - Fuhalf[j-1])
		nnew[j] = nold[j] - 2*defac*(Fnhalf[j] - Fnhalf[j-1])
	# For boundary grid points use forward (x = 0) and backward (x = 1)
	# differencing. Apply boundary conditions.
	unew[0] = u0 # boundary condition
	unew[J] = u1 # boundary condition
	nnew[0] = nold[0] - 2*defac*(Fnhalf[0] - Fn[0]) # forward difference
	nnew[J] = nold[J] - 2*defac*(Fn[J] - Fnhalf[J-1]) # backward difference
	# Update arrays with new values
	uold = np.copy(unew)
	nold = np.copy(nnew)
	line[0].set_ydata(nold)
	ax.set_title('Time = {0} s'.format(t))
	plt.draw()
	# Track the wave at timesteps we are interested in.
	if any(abs(t-stimes) < eps):
		savetimes.append(nold)
	t += tdel # update time to next timestep

################################## PLOT ##################################
plt.figure()
for i in range(len(savetimes)):
	plt.plot(x,savetimes[i],label = 't = {0} s'.format(stimes[i]))
plt.xlim(min(x),max(x))
plt.legend(loc = 'best')
plt.xlabel('$x [m]$',fontsize = 20)
plt.ylabel('$\eta$',fontsize = 20)
plt.title('Evolution of a shallow water wave over time using the TSLW scheme')




