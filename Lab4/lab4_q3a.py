import numpy as np
import matplotlib.pyplot as plt

def f(x,c):
	return 1-np.exp(-c*x)

cs = np.arange(0,3,0.01)
x0 = 1
eps = 1e-6

xi = x0
while True:
	xf = f(xi,c)
	if abs(xf-xi) > eps:
		xi = xf
	elif abs(xf-xi) < eps:
		break