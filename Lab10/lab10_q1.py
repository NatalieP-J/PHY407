from random import random, seed
import matplotlib.pyplot as plt
from numpy import copy
from time import sleep
plt.ion()

seed(43)#seed(56)

def move(i):
	inew = copy(i)
	diri = 2*random()
	if diri < 1:
		inew += 1
		if inew == L-1:
			inew -= 2
	if 1 < diri < 2:
		inew -= 1
		if inew == 0:
			inew += 2
	return inew

L = 101

i = int(L*random())
j = int(L*random())


nstep = 0

fig = plt.figure()
ax = plt.axes(xlim = (0,100),ylim = (0,100))
line = ax.plot(i,j,'o',markersize = 10)
ax.set_xlabel('i')
ax.set_ylabel('j')

ilist = []
jlist = []
while nstep <= int(1e6):
	i = move(i)
	j = move(j)
	ilist.append(i)
	jlist.append(j)
	line[0].set_xdata(i)
	line[0].set_ydata(j)
	ax.set_title('Step {0}'.format(nstep))
	plt.draw()
	nstep += 1

