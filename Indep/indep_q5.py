import numpy as np
import matplotlib.pyplot as plt

R = 10.
T0 = 50.
c = 1.25
eps = 1e-4

xmin = 0
xmax = R
delx = 0.01
x = np.arange(xmin,xmax + delx,delx)

tmin = 0
tmax = 100.
delt = 0.01
t = np.arange(tmin,tmax + delt,delt)

uinit = np.ones(len(x))*T0
ubc = 0.0
uinit[-1] = ubc

plt.figure()
ax = plt.axes(xlim = (xmin,xmax),ylim = (0,1000))
line = ax.plot(x,uinit)
plt.draw()

u = uinit
unew = np.zeros(np.shape(u))
usaves = []

for i in range(len(t)):
    if (t[i]-0) < eps or (t[i]-0.005) < eps or (t[i]-10.) < eps or (t[i]<100.) < eps:
        usaves.append(u)
    unew[2:-2] = u[2:-2] + ((c*delt)/(2*delx))*(((u[3:-1] - u[1:-3])/x[2:-2]) + ((u[4:] - 2*u[2:-2] + u[0:-4])/(2*delx)))
    unew[0:2] = u[0:2] + ((c*delt)/(delx))*(((u[1:3] - u[0:2])/(x[0:2])) + ((u[2:4] + u[0:2])/(delx)))
    unew[-2:] = u[-2:] + ((c*delt)/(delx))*(((u[-2:] - u[-3:-1])/(x[-2:])) + ((u[-2:] + u[-4:-2])/(delx)))
    unew[-1] = ubc
    if np.mod(i,100) == 0:
        line[0].set_ydata(unew)
        ax.set_title('t = {0} s'.format(i*delt))
        plt.draw()
    u = unew
    
    
        
