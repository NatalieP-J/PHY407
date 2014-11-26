import numpy as np
from random import random,randrange
import matplotlib.pyplot as plt

def energy(ss):
    lrarray = ss.flatten()
    lr = np.sum(lrarray[0:-1]*lrarray[1:])
    udarray1 = ss[0:-1].T.flatten()
    udarray2 = ss[1:].T.flatten()
    ud = np.sum(udarray1*udarray2)
    return -J*(lr+ud)

def magnet(ss):
    return np.sum(ss)

def metro_accept(E1,E2):
    if E2 <= E1:
        return True
    elif E2 > E1:
        P = np.exp(-beta*(E2-E1))
        z = random()
        if z <= P:
            return True
        elif z > P:
            return False

J = 1
T = 1
kb = 1
beta = 1./(T*kb)
ndip = 20
niter = int(1e5)

ss = np.random.randint(0,2,(ndip,ndip))
ss[np.where(ss==0)] = -1

energies = []
magnets = []

energies.append(energy(ss))
magnets.append(magnet(ss))

i = 0

while i < niter:
    newss = np.copy(ss)
    if (newss == -np.ones((ndip,ndip))).all() == True or (newss == np.ones((ndip,ndip))).all() == True:
        i = niter
    x,y = randrange(0,ndip),randrange(0,ndip)
    newss[x][y] *= -1
    enew = energy(newss)
    accept = metro_accept(energies[-1],enew)
    if accept == True:
        ss = newss
        energies.append(enew)
        magnets.append(magnet(newss))
        i+=1

plt.figure()
plt.subplot(211)
plt.plot(energies)
plt.ylabel('Energy')
plt.subplot(212)
plt.plot(magnets)
plt.xlabel('Step Number')
plt.ylabel('Magnetization')
