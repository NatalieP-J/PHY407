import numpy as np
import matplotlib.pyplot as plt
from time import clock

G = 39.5 #AU^3/Msun * yr^2
M = 1.98e30 #kg
AU = 1.496e11 #m
yr = 3600.*24.*365.

x0 = 4e12/AU #AU
y0 = 0 #AU
vx0 = 0 #AU/yr
vy0 = (500/AU)*yr #AU/yr

h = 1e-3

eps = 1e-3

def s(v):
    vx,vy = v
    return np.array([vx,vy])

def f(r):
    x,y = r
    rval = np.sqrt(x**2 + y**2)
    return (-G/rval**3)*np.array([x,y])

def RK4(h,r,fn):
    k1 = h*fn(r)
    k2 = h*fn(r+0.5*k1)
    k3 = h*fn(r+0.5*k2)
    k4 = h*fn(r+k3)
    #print (1./6.)*(k1 + 2*k2 + 2*k3 + k4)
    return r+(1./6.)*(k1 + 2*k2 + 2*k3 + k4)

start = clock()

orbits = 0

xs = np.array([])
ys = np.array([])

rs = []
vs = []

i = 0
r0 = np.array([x0,y0])
v0 = np.array([vx0,vy0])
r1 = r0
v1 = v0
while i < 50:
    r1 = RK4(h,v1,s)
    v1 = RK4(h,r1,f)
    xs = np.append(xs,r1[0])
    ys = np.append(ys,r1[1])
    rs.append(r1)
    vs.append(v1)
    i += 1
    if abs(r1[0]-x0) <= h and abs(r1[1] - y0) <= h:
        orbits +=1

end = clock()
    

print 'Time to run: ', end - start,' s'

plt.plot(xs,ys,'o')
plt.show()
