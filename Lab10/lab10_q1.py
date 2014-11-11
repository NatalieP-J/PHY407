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

L = 101

i = L/2 + 1
j = L/2 + 1


nstep = 0

fig = plt.figure()
ax = plt.axes(xlim = (0,L),ylim = (0,L))
line = ax.plot(i,j,'o',markersize = 10)
ax.set_xlabel('i')
ax.set_ylabel('j')

ilist = []
jlist = []
nmax = 10000
while nstep <= nmax:
	i,j = move(i,j,L)
	ilist.append(i)
	jlist.append(j)
	line[0].set_xdata(i)
	line[0].set_ydata(j)
	ax.set_title('Step {0}'.format(nstep))
	plt.draw()
	nstep += 1

plt.figure()
plt.title('Trajectory of Particle after N = {0} steps of Brownian Motion'.format(nmax))
plt.xlabel('i')
plt.ylabel('j')
plt.plot(ilist,jlist)


