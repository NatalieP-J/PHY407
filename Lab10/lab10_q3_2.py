from random import randrange, seed
import matplotlib.pyplot as plt
from numpy import copy,array,where
from time import sleep
plt.ion()

###############################################################################

# This code takes a particle on a random walk until it reaches the boundary of 
# the grid or is adjacent to another particle. Then it stops moving that
# particle and spawns another, repeating the process until the maximum number
# of particles is reached.

################################## CONSTANTS ##################################

# Set to True to animate the random walk
animate = False
# Choose seed to check results can be reproduced
seed(42)
# Size of grid 
L = 101

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
	if diri == 2:
		inew -= 1
	if diri == 3:
		jnew += 1
	if diri == 4:
		jnew -= 1
	return inew,jnew

# Performs all necessary tasks when the particle is finished its walk:
# adds its position to the array and tells it to stop walking (and updates
# the animation, if necessary)
def donewalk(i,j,anchor):
	anchor.append([i,j])
	if animate == True:
		ax1.plot(array(anchor)[:,0],array(anchor)[:,1],'go',markersize = 10)
		plt.draw()
	walk = False
	return walk,anchor 

# Checks if a particle at i,j is adjacent to any anchored particles
def checkadjacent(i,j,anchor):
	if anchor != []:
		iloc = where(array(anchor)[:,0] == i)[0]
		jloc = where(array(anchor)[:,1] == j)[0]
		iuloc = where(array(anchor)[:,0] == i+1)[0]
		idloc = where(array(anchor)[:,0] == i-1)[0]
		juloc = where(array(anchor)[:,1] == j+1)[0]
		jdloc = where(array(anchor)[:,1] == j-1)[0]
		m1 = [n for n in iloc if n in juloc]
		m2 = [n for n in iloc if n in jdloc]
		l1 = [n for n in jloc if n in iuloc]
		l2 = [n for n in jloc if n in juloc]
		if m1 != [] or m2 !=[] or l1 != [] or l2 != []:
			return True
		else:
			return 'no match'
	elif anchor == []:
		return 'anchor empty'

	'''
	for k in range(len(anchor)):
		if i == anchor[k][0] and j == anchor[k][1]:
			return False
		if i == anchor[k][0] and j != anchor[k][1]:
			if (j+1) == anchor[k][1] or (j-1) == anchor[k][1]:
				return True
		if j == anchor[k][1] and i != anchor[k][1]:
			if (i+1) == anchor[k][0] or (i-1) == anchor[k][0]:
				return True
	'''

################################## MAIN PROGRAM ##################################

# Choose start positions for each particle
istart = L/2 + 1
jstart = L/2 + 1

# If we wish to animate the walk, initialize updating figure

if animate == True:
	fig = plt.figure()
	ax = plt.axes(xlim = (0,L),ylim = (0,L)) #random walking particle positions
	ax1 = plt.axes(xlim = (0,L),ylim = (0,L)) #anchor particle positions
	line = ax.plot(istart,jstart,'bo',markersize = 10)
	ax.set_xlabel('i')
	ax.set_ylabel('j')

# Create empty list to hold anchored particle coordinates
anchor = []

# Choose starting particle index
npart = 0

while [istart,jstart] not in anchor:
	print 'Particle {0}'.format(npart+1) 	
	# For each particle, set its starting position
	i,j = istart,jstart
	# Tell the particle to begin walking
	walk = True
	while walk == True:
		# Update position
		i,j = move(i,j,L)
		# If the particle hits a boundary, stop walking and anchor it
		if i == L or j == L or i == 0 or j == 0:
			walk,anchor = donewalk(i,j,anchor)
		# Otherwise, check if it is adjacent to another particle
		else:		
			match = checkadjacent(i,j,anchor)
			if match == True:
				walk,anchor = donewalk(i,j,anchor)
	# Once walking is stopped, go to next particle
	npart += 1

anchor = array(anchor)

################################## PLOT ##################################

plt.figure()
plt.title('Final positions of particles in diffusion limited aggregation')
plt.xlabel('i')
plt.ylabel('j')
plt.plot(anchor[:,0],anchor[:,1],'go',markersize = 10)
plt.xlim(0,L)
plt.ylim(0,L)

