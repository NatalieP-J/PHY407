import numpy as np
import matplotlib.pyplot as plt

G = 6.674 * 1e-11 #m^3 kg^-1 s^-2
M = 5.974 * 1e24 #kg
m = 7.348 * 1e22 #kg
R = 3.844 * 1e8 #m
w = 2.662 * 1e-6 #s^-1

def f(r):
	return (G*M/r**2) - (G*m/(R-r)**2) - r*w**2

def f(x):
	return x*(x - 10)

def secant(initial,fn,tol):
	x1,x2 = initial
	i = 0
	while i < 10:
		print i
		fprime = (f(x2) - f(x1))/(x1-x2) 
		print x1,x2,fprime
		x3 = x2 - fn(x2)*(1./fprime)
		print x3
		print x3-x2
		if abs(x3 - x2) > tol:
			x1 = x2
			x2 = x3
			i+=1
		elif abs(x3 - x2) < tol:
			break
	return x3,i

#r1 = 10**8.3
#r2 = 10**8.5
r1 = 7.
r2 = 13.
L0 = r2 - f(r2)*((r2-r1)/(f(r2) - f(r1)))
eps = 1e-6

x1 = r1
x2 = r2

x3,i = secant([r1,r2],f,eps)

print 'L1 = ',x3,'\tf(L1) = ',f(x3),'\nnumber of iterations: ',i 

