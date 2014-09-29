import numpy as np
import matplotlib.pyplot as plt

G = 6.674 * 1e-11 #m^3 kg^-1 s^-2
M = 5.974 * 1e24 #kg
m = 7.348 * 1e22 #kg
R = 3.844 * 1e8 #m
w = 2.662 * 1e-6 #s^-1

def f(r):
	return (G*M/r**2) - (G*m/(R-r)**2) - r*w**2

#r1 = 0.10*R
#r2 = 0.30*R
r1 = 0.10*R
r2 = 3*R
L0 = r2 - f(r2)*((r2-r1)/(f(r2) - f(r1)))
eps = 1e-9

x1 = r1
x2 = r2
i = 0
while True:
	L1 = x2 - f(x2)*((x2-x1)/(f(x2) - f(x1)))
	if abs(L1 - x2) > eps:
		x1 = x2
		x2 = L1
		i += 1
	if abs(L1 - x2) < eps:
		print 'Final iteration difference: {0} - {1} = {2}'.format(L1,x2,abs(L1-x2))
		break

print 'L1 = ',L1,'\tf(L1) = ',f(L1),'\nnumber of iterations: ',i 

