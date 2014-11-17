from random import randrange, seed
import matplotlib.pyplot as plt
from numpy import copy,array
from time import sleep
plt.ion()

seed(42)#seed(56)

animate = False

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

def donewalk(i,j,anchor):
	anchor.append([i,j])
	if animate == True:
		ax1.plot(array(anchor)[:,0],array(anchor)[:,1],'go',markersize = 10)
		plt.draw()
	walk = False
	return walk,anchor 

def checkadjacent(i,j,anchor):
	for k in range(len(anchor)):
		if i == anchor[k][0] and j == anchor[k][1]:
			return False
		if i == anchor[k][0] and j != anchor[k][1]:
			if (j+1) == anchor[k][1] or (j-1) == anchor[k][1]:
				return True
		if j == anchor[k][1] and i != anchor[k][1]:
			if (i+1) == anchor[k][0] or (i-1) == anchor[k][0]:
				return True

L = 100

istart = L/2 + 1
jstart = L/2 + 1


npart = 0

if animate == True:
	fig = plt.figure()
	ax = plt.axes(xlim = (0,L),ylim = (0,L))
	ax1 = plt.axes(xlim = (0,L),ylim = (0,L))
	line = ax.plot(istart,jstart,'bo',markersize = 10)
	ax.set_xlabel('i')
	ax.set_ylabel('j')

anchor = []
parti = []
partj = []
Npart = 100
while npart < Npart:
	if [istart,jstart] in anchor:
		print 'Particles extend to start point, quitting'
		npart = Npart
	print 'Particle {0} of {1}'.format(npart+1,Npart) 	
	i,j = istart,jstart
	walk = True
	part1 = []
	part2 = []
	while walk == True:
		i,j = move(i,j,L)
		part1.append(i)
		part2.append(j)
		if animate == True:
			line[0].set_xdata(i)
			line[0].set_ydata(j)
			ax.set_title('Particle {0}'.format(npart+1))
			plt.draw()
		if i == L or j == L or i == 0 or j == 0:
			walk,anchor = donewalk(i,j,anchor)
		else:
			match = checkadjacent(i,j,anchor)
			if match == True:
				walk,anchor = donewalk(i,j,anchor)
			if match == False:
				npart -= 1
				walk = False
	parti.append(part1)
	partj.append(part2)
	npart += 1

anchor = array(anchor)

plt.figure()
plt.title('Final positions of particles in diffusion limited aggregation')
plt.xlabel('i')
plt.ylabel('j')
plt.plot(anchor[:,0],anchor[:,1],'go',markersize = 10)
plt.xlim(0,L)
plt.ylim(0,L)

