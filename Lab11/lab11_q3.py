from numpy import arange,array,where
from random import randrange
import matplotlib.pyplot as plt
from time import sleep
plt.ion()

def adjacentpt(x,y):
    z = randrange(0,4)
    if z == 0:
        return x,y+1
    if z == 1:
        return x,y-1
    if z == 2:
        return x+1,y
    if z == 3:
        return x-1,y

def energy(dimerlist):
    return -len(dimerlist)

L = 50
dimer = []
dimerpl = []
empty = []
for l1 in range(L):
    for l2 in range(L):
        empty.append([l1,l2])
iterations = 1000

plt.figure()
ax = plt.axes(xlim = (-0.5,L+0.5),ylim = (-0.5,L+0.5))
ax.vlines(arange(-1,L+1)+0.5,-0.5,L+0.5)
ax.hlines(arange(-1,L+1)+0.5,-0.5,L+0.5)

for i in range(iterations):
    x1 = randrange(0,L)
    y1 = randrange(0,L)
    x2,y2 = adjacentpt(x1,y1)
    if [x2,y2] in empty and [x1,y1] in empty:
        dimer.append([[x1,y1],[x2,y2]])
        ax.plot([x1,x2],[y1,y2],'-o',color = 'b')
        plt.draw()
        empty.remove([x1,y1])
        empty.remove([x2,y2])
    elif [[x1,y1],[x2,y2]] in dimer:
        k = dimer.index([[x1,y1],[x2,y2]])
        ax.lines.pop(k)
        plt.draw()
        dimer.remove([[x1,y1],[x2,y2]])
        empty.append([x1,y1])
        empty.append([x2,y2])
    elif [[x2,y2],[x1,y1]] in dimer:
        k = dimer.index([[x2,y2],[x1,y1]])
        ax.lines.pop(k)
        plt.draw()
        dimer.remove([[x2,y2],[x1,y1]])
        empty.append([x1,y1])
        empty.append([x2,y2])

