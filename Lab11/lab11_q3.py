from numpy import arange,array,where,copy,exp
from random import randrange,random
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

def metro_accept(E1,E2,temp):
    if E2 <= E1:
        return True
    elif E2 > E1:
        beta = 1./(temp*kb)
        P = exp(-beta*(E2-E1))
        z = random()
        if z <= P:
            return True
        elif z > P:
            return False

T0 = 1e-5
tau = 10000
t = arange(float(tau))
T = T0*exp(-t/float(tau))
kb = 1

L = 50
dimer = []
dtemp = []
dimerpl = []
empty = []
for l1 in range(L):
    for l2 in range(L):
        empty.append([l1,l2])

etemp = empty

energies = []

plt.figure()
ax = plt.axes(xlim = (-0.5,L-0.5),ylim = (-0.5,L-0.5))
ax.vlines(arange(-1,L+1)+0.5,-0.5,L+0.5)
ax.hlines(arange(-1,L+1)+0.5,-0.5,L+0.5)

i = 0
while i < tau:
    x1 = randrange(0,L)
    y1 = randrange(0,L)
    x2,y2 = adjacentpt(x1,y1)
    if [x2,y2] in empty and [x1,y1] in empty:
        dtemp.append([[x1,y1],[x2,y2]])
        ax.plot([x1,x2],[y1,y2],'-o',color = 'b')
        plt.draw()
        etemp.remove([x1,y1])
        etemp.remove([x2,y2])
    elif [[x1,y1],[x2,y2]] in dimer:
        k = dimer.index([[x1,y1],[x2,y2]])
        ax.lines.pop(k)
        plt.draw()
        dtemp.remove([[x1,y1],[x2,y2]])
        etemp.append([x1,y1])
        etemp.append([x2,y2])
    elif [[x2,y2],[x1,y1]] in dimer:
        k = dimer.index([[x2,y2],[x1,y1]])
        ax.lines.pop(k)
        plt.draw()
        dtemp.remove([[x2,y2],[x1,y1]])
        etemp.append([x1,y1])
        etemp.append([x2,y2])
    enew = energy(dtemp)
    if i != 0:
        accept = metro_accept(energies[-1],enew,T[i])
        if accept == True:
            energies.append(enew)
            dimer = dtemp
            empty = etemp
            i+=1
    if i == 0:
        energies.append(enew)
        dimer = dtemp
        empty = etemp

plt.figure()
plt.plot(energies)


