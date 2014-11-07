from random import random, seed
import matplotlib.pyplot as plt
from numpy import copy,where
from time import sleep
plt.ion()

seed(43)#seed(56)

def move(i):
	inew = copy(i)
	diri = 2*random()
	if diri < 1:
		inew += 1
		if inew == L+1:
			inew -= 1
	if 1 < diri < 2:
		inew -= 1
		if inew == -1:
			inew += 1
	return inew

def donewalk(i,j,npart):
	anchori.append(int(i))
	anchorj.append(int(j))
	ax1.plot(anchori,anchorj,'go',markersize = 10)
	npart += 1
	return False,npart

def failwalk(i,j,npart):
	return False,npart

def indlocate(ival,ilist):
	return [i for i, j in enumerate(ilist) if j == ival]

def intersect(list1,list2):
	return [i for i in list1 if i in list2]

L = 11#101

N = 50

anchori = []
anchorj = []

istart = L/2 + 1
jstart = L/2 + 1

npart = 1

fig = plt.figure()
ax = plt.axes(xlim = (0,L),ylim = (0,L))
ax1 = plt.axes(xlim = (0,L),ylim = (0,L))
line = ax.plot(istart,jstart,'o',markersize = 10)
ax.set_xlabel('i')
ax.set_ylabel('j')

while npart < N:
	i,j = istart,jstart
	walk = True
	while walk == True:
		i = move(i)
		j = move(j)
		line[0].set_xdata(i)
		line[0].set_ydata(j)
		plt.draw()
		if i == 0 or j == 0 or i == L or j == L:
			walk,npart = donewalk(i,j,npart)
		elif i in anchori and j not in anchorj:
			print 'possible adjacent'
			iloc = indlocate(i,anchori)
			jlocup = indlocate(j+1,anchorj)
			jlocdown = indlocate(j-1,anchorj)
			print iloc,jlocup,jlocdown
			if intersect(iloc,jlocup) != [] or intersect(iloc,jlocdown) != []:#iloc == jlocup or iloc == jlocdown:
				print 'i,j = ', i,j
				walk,npart = donewalk(i,j,npart)
		elif j in anchorj and i not in anchori:
			print 'possible adjacent'
			jloc = indlocate(j,anchorj)
			ilocup = indlocate(i+1,anchori)
			ilocdown = indlocate(i-1,anchori)
			print jloc,ilocup,ilocdown
			if intersect(jloc,ilocup) != [] or intersect(jloc,ilocdown) != []:#jloc == ilocup or jloc == ilocdown:
				print 'i,j = ', i,j
				walk,npart = donewalk(i,j,npart)
		elif i in anchori and j in anchorj:
			iloc = indlocate(i,anchori)
			jloc = indlocate(j,anchorj)
			if iloc == jloc:
				walk,npart = failwalk(i,j,npart)

ax1.plot(anchori,anchorj,'go',markersize = 10)

