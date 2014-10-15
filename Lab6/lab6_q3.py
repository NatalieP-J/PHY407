import numpy as np
import matplotlib.pyplot as plt
from time import clock

G = 39.5 #AU^3/Msun * yr^2
M = 1. #Msun
AU = 1.496e11 #m
yr = 3600.*24.*365.

x0 = 4.e12/AU #AU
y0 = 0 #AU
vx0 = 0 #AU/yr
vy0 = (5.e2/AU)*yr #AU/yr

h0 = 0.0005
hmax = 50.*h0
totaltime = 100.
delta = 1.e3/AU

def f(r):
    x,y,vx,vy = r
    rval = np.sqrt(x**2 + y**2)
    dxdt = vx
    dydt = vy
    dvxdt = -(G*M/rval**3)*x
    dvydt = -(G*M/rval**3)*y
    return np.array([dxdt,dydt,dvxdt,dvydt])

def RK4(h,r,fn):
    k1 = h*fn(r)
    k2 = h*fn(r+0.5*k1)
    k3 = h*fn(r+0.5*k2)
    k4 = h*fn(r+k3)
    return np.array(r+(1./6.)*(k1 + 2*k2 + 2*k3 + k4))

start = clock()

orbits = 0

rs = []
t = []
time = 0
r0 = np.array([x0,y0,vx0,vy0])
rs.append(r0)
t.append(time)
h = h0
while time < totaltime:
    rnew1half = RK4(h,r0,f)
    rnew1 = RK4(h,rnew1half,f)
    rnew2 = RK4(2.*h,r0,f)
    xerr = (1./30.)*(rnew1[0]-rnew2[0])
    yerr = (1./30.)*(rnew1[1]-rnew2[1])
    rho = h*delta/(xerr**2 + yerr**2)**0.5
    if np.isinf(rho) == True:
        h = hmax
    elif rho > 1:
        time += h
        t.append(time)
        r0 = rnew1half
        h *= rho**0.25
        rs.append(rnew1half)
    elif rho < 1:
        h *= rho**0.25

end = clock()

rs = np.array(rs)    

t = np.array(t)

print 'Time to run: ', end - start,' s'

rvals = np.sqrt(rs[:,0]**2 + rs[:,1]**2)

plt.figure()
plt.plot(rs[:,0][0::20],rs[:,1][0::20],'.')
plt.plot(0,0,'y*',markersize = 15)
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.title('Integration positions of fourth order Runge-Kutta method (every 20th step shown)')

'''plt.figure()
plt.subplot(211)
plt.plot(t,rs[:,0])
plt.subplot(212)
plt.plot(t,rs[:,1])
plt.figure()
plt.plot(t,rvals)'''
plt.show()