from random import random, seed
import matplotlib.pyplot as plt
from numpy import copy,where,array,append,zeros
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
	return False,npart+1

def failwalk(i,j,npart):
	return False,npart

L = 21#101

N = 7

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
		#print 'i,j = ',i,j
		line[0].set_xdata(i)
		line[0].set_ydata(j)
		plt.draw()
		absi = abs(i-array(anchori))
		absj = abs(j-array(anchorj))
		#print 'absi = ',absi
		#print 'absj = ',absj
		mi = where(absi == 0)[0]
		mj = where(absj == 0)[0]
		ni = where(absi == 1)[0]
		nj = where(absj == 1)[0]
		mint = [i for i in mi if i in mj]
		nint1 = [i for i in ni if i in mj]
		nint2 = [i for i in nj if i in mi]
		if mint != []:
			print 'overlapped'
			print 'mint = ',mint
			walk,npart = failwalk(i,j,npart)
		elif nint1 != [] or nint2 != []:
			print 'added sticky anchor'
			print 'nint1 = ',nint1, 'nint2 = ',nint2
			walk,npart = donewalk(i,j,npart)
		elif i == 0 or j == 0 or i == L or j == L:
			print 'added border anchor'
			walk,npart = donewalk(i,j,npart)
ax1.plot(anchori,anchorj,'go',markersize = 10)

