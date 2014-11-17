from random import randrange, seed
import matplotlib.pyplot as plt
from numpy import copy,zeros
from time import sleep
plt.ion()

###############################################################################

# This code takes a particle on a random walk

################################## CONSTANTS ##################################

# Set to True to animate the random walk
animate = False
# Choose seed to check results can be reproduced
seed(42)
# Size of grid 
L = 101
# Maximum number of steps the particle will take
nmax = int(5e3)

################################## FUNCTIONS ##################################

# Moves a particle a i,j on an integer grid with size L randomly in one of the 
# following directions: up, down, left or right. If the particle reaches
# a boundary of the grid, it undoes that step and takes another in one of the 
# three remaining directions
def move(i,j,L):
	inew,jnew = copy(i),copy(j)
	diri = randrange(1,5)
	if diri == 1:
		inew += 1
		if inew > L:
			inew,jnew = move(inew-1,jnew,L)
	if diri == 2:
		inew -= 1
		if inew < 0:
			inew,jnew = move(inew+1,jnew,L)
	if diri == 3:
		jnew += 1
		if jnew > L:
			inew,jnew = move(inew,jnew-1,L)
	if diri == 4:
		jnew -= 1
		if jnew < 0:
			inew,jnew = move(inew,jnew+1,L)
	return inew,jnew

################################## MAIN PROGRAM ##################################

# If we wish to animate the walk, initialize updating figure

if animate == True:
	fig = plt.figure()
	ax = plt.axes(xlim = (0,L),ylim = (0,L))
	line = ax.plot(i,j,'o',markersize = 10)
	ax.set_xlabel('i')
	ax.set_ylabel('j')

# Choose start position for particle
i = L/2 + 1
j = L/2 + 1

# Set initial step number
nstep = 0

# Create empty arrays to hold 
ilist = zeros(nmax)
jlist = zeros(nmax)

# For each step, move the particle randomly
while nstep < nmax:
	i,j = move(i,j,L)
	# Store the particle's position
	ilist[nstep] = i
	jlist[nstep] = j
	if animate == True:
		line[0].set_xdata(i)
		line[0].set_ydata(j)
		ax.set_title('Step {0}'.format(nstep))
		plt.draw()
	nstep += 1

################################## PLOT ##################################
plt.figure()
plt.title('Trajectory of Particle after N = {0} steps of Brownian Motion'.format(nmax))
plt.xlabel('i')
plt.ylabel('j')
plt.plot(ilist,jlist)
plt.xlim(0,L)
plt.ylim(0,L)


