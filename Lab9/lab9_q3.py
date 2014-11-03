import numpy as np
import matplotlib.pyplot as plt
from dcst import dst,idst
plt.ion()


m = 9.109e-31 #kg
L = 1e-8 #m
x0 = L/2. #m
sig = 1e-10 #m
kap = 5e10 #m^-1
hbar = 1.055e-34 #m^2 kg/s
N = 1000
a = float(L/N) #m
h = 1e-16 #s
x = np.arange(0,L,a)

psi = np.zeros(len(x),complex)
psi0 = 0.
psi1 = 0.
psi_init = np.exp(-(x[1:len(x)-2] - x0)**2/(2*sig**2))*np.exp(1j*kap*x[1:len(x)-2])
psi[0] = psi0
psi[-1] = psi1
psi[1:len(x)-2] = psi_init

psiR = psi.real
psiI = psi.imag

alpha = dst(psiR)
eta = dst(psiI)

plt.plot(np.abs(alpha + 1j*eta))
plt.ylabel('$|b_k|$',fontsize = 20)
plt.xlabel('$k$',fontsize = 20)
plt.title('Fourier Coefficients')

k = np.arange(0,len(alpha))

arg = (hbar/(2*m))*(np.pi*k/L)**2

fig = plt.figure()
ax = plt.axes()
line = ax.plot(x,psi.real)
ax.set_xlabel('$x [m]$',fontsize = 20)
ax.set_ylabel('$\psi$',fontsize = 20)

t = 0
while t < h*100:
    line[0].set_ydata(psi.real)
    ax.set_title('Time = {0} s'.format(t))
    plt.draw()
    alphan = alpha * np.cos(arg*t)
    etan = eta*np.sin(arg*t)
    psi = idst(alphan) - idst(etan)
    psi[0] = psi0
    psi[-1] = psi1
    t+=h


