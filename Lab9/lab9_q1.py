import numpy as np
import matplotlib.pyplot as plt
from banded import banded
import cmath as cm
plt.ion()


m = 9.109e-31 #kg
L = 1e-8 #m
x0 = L/2. #m
sig = 1e-10 #m
kap = 5e10 #m^-1
hbar = 1.055e-34 #m^2 kg/s

N = 1000
a = float(L/N) #m
h = 1e-18 #s
x = np.arange(0,L,a)
ele = h*(1j*hbar/(4*m*a**2))
a1 = 1 + 2*ele
a2 = -ele
b1 = 1 - 2*ele
b2 = ele

def vvec(psi):
    v = np.zeros(len(psi),complex)
    v[0] = b1*psi[0] + b2*psi[1]
    v[-1] = b1*psi[-1] + b2*psi[-2]
    for i in range(1,len(psi)-1):
        v[i] = b1*psi[i] + b2*(psi[i+1] + psi[i-1])
    return v


A = np.zeros((len(x),len(x)),complex)

for i in range(len(A)):
    for j in range(i-1,i+2):
        if i == j:
            A[i][j] = a1
        elif i != j:
            if i != (len(x)-1) and i != 0:
                A[i][j] = a2
            elif i == (len(x) - 1):
                A[i][i-1] = a2
            elif i == 0:
                A[i][i+1] = a2

psi = np.zeros(len(x),complex)
psi0 = 0.
psi1 = 0.
psi_init = np.exp(-(x[1:len(x)-2] - x0)**2/(2*sig**2))*np.exp(1j*kap*x[1:len(x)-2])
psi[0] = psi0
psi[-1] = psi1
psi[1:len(x)-2] = psi_init


fig = plt.figure()
ax = plt.axes()
line = ax.plot(x,psi.real)
ax.set_xlabel('$x [m]$',fontsize = 20)
ax.set_ylabel('$\psi$',fontsize = 20)

t = 0
while t < 100*h:
    line[0].set_ydata(psi.real)
    ax.set_title('Time = {0} s'.format(t))
    plt.draw()
    v = vvec(psi)
    #print v
    psi = np.linalg.solve(A,v)
    t+=h
