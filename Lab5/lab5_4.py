import numpy as np
import matplotlib.pyplot as plt
import cmath as cm

sw = 20.* 1e-6 #m
w = 200. * 1e-6 #m
W = 10.*w #m
lam = 500. * 1e-9 #m
sl = 10. * 1e-2 #m
f = 1. #m

alpha = np.pi/sw

N = 400 #N=400 gives right width

def q(u):
	return np.sin(alpha*u)**2

def I(ck):
	Is = (W/N)**2 * abs(ck)**2
	xs = (lam*f/W)*np.arange(0,len(ck))
	return xs,Is

us = np.linspace(-w/2.,w/2.,N)

cks = np.fft.rfft(np.sqrt(q(us)))

flip = cks[:len(cks)-1][::-1]
for k in range(len(flip)):
	flip[k] = cks[k].conjugate()

cks_full = np.concatenate((cks,flip))

xs,Is = I(cks_full)

plt.plot(xs-0.05,Is)
plt.show()
