from random import randrange, seed
import matplotlib.pyplot as plt
from numpy import copy
from time import sleep
plt.ion()

seed(43)#seed(56)

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

def donewalk(i,j,ianchor,janchor):
	ianchor.append(i)
	janchor.append(j)
	ax1.plot(ianchor,janchor,'go',markersize = 10)
	walk = False
	return walk 

def checkadjacent(matchval,otherval,list1,list2):
	loc = []
	up = otherval + 1
	down = otherval - 1
	for k in range(len(list1)):
		if matchval == list1[k]:
			loc.append(k)
	for m in range(len(loc)):
		if up == list2[loc[m]] or down == list2[loc[m]]:
			return True
		else:
			return False
L = 5

istart = L/2 + 1
jstart = L/2 + 1


npart = 0

fig = plt.figure()
ax = plt.axes(xlim = (0,L),ylim = (0,L))
ax1 = plt.axes(xlim = (0,L),ylim = (0,L))
line = ax.plot(istart,jstart,'bo',markersize = 10)
ax.set_xlabel('i')
ax.set_ylabel('j')

ianchor = []
janchor = []
parti = []
partj = []
Npart = 10
while npart <= Npart:
	i,j = istart,jstart
	walk = True
	part1 = []
	part2 = []
	while walk == True:
		i,j = move(i,j,L)
		part1.append(i)
		part2.append(j)
		sleep(0.5)
		line[0].set_xdata(i)
		line[0].set_ydata(j)
		ax.set_title('Particle {0}'.format(npart+1))
		plt.draw()
		if i == L or j == L or i == 0 or j == 0:
			walk = donewalk(i,j,ianchor,janchor)
		elif any(ianchor) == i:
			match = checkadjacent(i,j,ianchor,janchor)
			if match == True:
				walk = donewalk(i,j,ianchor,janchor)
		elif any(janchor) == j:
			match = checkadjacent(j,i,janchor,ianchor)
			if match == True:
				walk = donewalk(i,j,ianchor,janchor)
	parti.append(part1)
	partj.append(part2)
	npart += 1

plt.figure()
plt.title('Final positions of particles in diffusion limited aggregation')
plt.xlabel('i')
plt.ylabel('j')
plt.plot(ianchor,janchor,'go',markersize = 10)
plt.xlim(0,L)
plt.ylim(0,L)

