import numpy as np 
import matplotlib.pyplot as plt
import random

###############################################################################

# This code computes the movement of ten molecules in a Lennard-Jones potential
# interacting in a box with periodic boundary conditions. This is done by 
# integrating ODEs using the Verlet method with fixed timestep.

################################## FUNCTIONS ##################################

# A function that returns the acceleration experienced at each particle
# postion in r, assuming a 2D system
def dvdt2D(r):
	xs,ys = r[:,0],r[:,1]
	dvdts = []
	for i in range(len(r)):
		Fix = 0
		Fiy = 0
		for j in range(len(r)):
			if j != i:
				rmag = ((xs[i]-xs[j])**2 + (ys[i]-ys[j])**2)**0.5
				Fix += ((xs[i]-xs[j])/rmag**8)*((2./rmag**6) - 1.)
				Fiy += ((ys[i]-ys[j])/rmag**8)*((2./rmag**6) - 1.)
		Fix *= 24
		Fiy *= 24
		dvdts.append([Fix,Fiy])
	return np.array(dvdts)

# A function that iterates through the Verlet method to find position
# and velocity of each particle at each time
def verlet_periodic(v0,r0,h,N,L,fn):
	"""
	v0 - initial particle velocities
	r0 - initial particle positions
	h - timestep size
	N - number of timesteps
	L - sidelength of square box where particles are constrained to lie
	fn - a function that returns the derivative of each velocity component
	returns positions and velocities for each particle at each timestep
	"""
	# Calculate half step velocity with Euler
	vhalf = v0 + 0.5*h*fn(r0)
	# Create empty arrays to hold resulting positions and velocities
	vs = []
	rs = []
	# Start iteration counter at zero
	i = 0
	while i < N:
		# Update positions such that they remain inside the box if
		# the particle has escaped
		r0 = np.mod(r0,L)
		# Add position to the array
		rs.append(np.copy(r0))
		# Update position estimate
		r0 += h*vhalf
		k = h*fn(r0)
		# Update velocity estimate and add it to the array
		v0 = vhalf + 0.5*k
		vs.append(np.copy(v0))
		# Update half step velocity
		vhalf += k
		i+=1
	return np.array(rs),np.array(vs)

################################## MAIN PROGRAM ##################################

# Choose time step size and number of time steps
dt = 0.01
nstep = 1.e2

# Create array of timestamps
t = np.arange(0,dt*nstep,dt)

# Choose number of particles and create arrays to hold initial information
npart = 10
rinit = []
vinit = []

# Randomly assign each particle an initial position
# Set all initial velocities to zero
for i in range(npart):
	vinit.append([0,0])
	x,y = random.uniform(1,9),random.uniform(1,9)
	rinit.append([x,y])

rinit = np.array(rinit)
vinit = np.array(vinit)

# Choose box side length
L = 10.

# Find the position and velocity of each particle for each timestamp
rs,vs = verlet_periodic(vinit,rinit,dt,nstep,L,dvdt2D)

################################## PLOT ##################################

# Choose a colour for each particle
colours = {0:'Crimson',1:'DeepSkyBlue',2:'Fuchsia',3:'HotPink',4:'LawnGreen',
		   5:'OrangeRed',6:'SeaGreen',7:'Tomato',8:'DarkOrange',9:'MediumVioletRed'}

# Plot each particle's trajectory
plt.figure()
for i in range(npart):
	particle = rs[:,i]
	x,y = particle[:,0],particle[:,1]
	plt.plot(x,y,'.',color = colours[i])

plt.xlim(0,10)
plt.ylim(0,10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectories of 10 particles interacting via Lennard-Jones potential')
plt.show()

