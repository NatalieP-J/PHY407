import numpy as np
import matplotlib.pyplot as plt

def f(x,c):
	return 1-np.exp(-c*x)

c = 2
x0 = 1
eps = 1e-6

xi = x0
i = 0
while True:
	xf = f(xi,c)
	if abs(xf-xi) > eps:
		xi = xf
		i+=1
	elif abs(xf-xi) < eps:
		break

print i,' iterations'