import numpy as np 
import matplotlib.pyplot as plt

###############################################################################

# This code computes the movement of two molecules in a Lennard-Jones potential.
# This is done by integrating ODEs using the Verlet method with fixed timestep.

################################## FUNCTIONS ##################################

# The Lennard-Jones potential where r is the separation between charges
def V(r):
	return (4./r**6)*((1./r**6) - 1.)

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
def verlet(v0,r0,h,N,fn):
	"""
	v0 - initial particle velocities
	r0 - initial particle positions
	h - timestep size
	N - number of timesteps
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
dt = 0.02
nstep = 1.e2
# Create array of timestamps
t = np.arange(0,dt*nstep,dt)

# Choose initial conditions by uncommenting any rinit below
rinit = np.array([[4.,4.],[6.,4.]]) # part a
#rinit = np.array([[4.9,4.],[5.1,4.]]) # part b
#rinit = np.array([[2.,3.],[7.,6.]]) # part c
#rinit = np.array([[3.5,4.5],[5.,3.5]]) # part d

# Set initial velocities to zero
vinit = np.array([[0,0],[0,0]])

# Calculate position and velocity for each time in t
rs,vs = verlet(np.copy(vinit),np.copy(rinit),dt,nstep,dvdt2D)

# Divide position results into the two particles
part1 = rs[:,0]
part2 = rs[:,1]

################################## PLOT ##################################

plt.figure()
plt.scatter(part1[:,0], part1[:,1], c=t[::-1], s=500)
plt.scatter(part2[:,0], part2[:,1], c=t[::-1], s=500)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trajectories of particles with starting positions ({0},{1}) and ({2},{3})'.format(rinit[0][0],rinit[0][1],rinit[1][0],rinit[1][1]))

plt.figure()
plt.subplot(211)
plt.scatter(t, part1[:,0], c=t[::-1], s=50)
plt.scatter(t, part2[:,0], c=t[::-1], s=50)
plt.xlim(min(t),max(t))
plt.ylabel('X position')
plt.legend(loc = 'best')
plt.subplot(212)
plt.scatter(t, part1[:,1], c=t[::-1], s=50)
plt.scatter(t, part2[:,1], c=t[::-1], s=50)
plt.xlabel('Time')
plt.ylabel('Y position')
plt.xlim(min(t),max(t))
plt.suptitle('Evolution of x and y position with time')

plt.show()
