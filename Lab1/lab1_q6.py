from numpy import *
import matplotlib.pyplot as plt

# This code finds the orbit of Mercury under the Sun's gravity (including 
# general relativity) for one Earth year with set initial conditions. All 
# distance units are AU, all mass units are Msun and all time units are years.

# Set the gravitational constant in astronomical units, years and the 
# mass of the sun. Set alpha for Mercury (modified for this problem).
G = 39.5 #AU^3/Ms*yr
alpha = 0.01 #AU^2

# Set start time, end time and the time step.
ti = 0 #yr
tf = 1 #yr
dt = 0.0001 #yr

# Create time array.
time = arange(ti,tf,dt)

# Create arrays to hold results for x,y position and velocity over the orbit.
x = zeros(len(time)) # x position
y = zeros(len(time)) # y position
r = zeros(len(time)) # Mercury's separation from the Sun
vx = zeros(len(time)) # x velocity
vy = zeros(len(time)) # y velocity

# Set initial x,y position and velocity
x[0] = 0.47 #AU
y[0] = 0.0 #AU
r[0] = (x[0]**2 + y[0]**2)**0.5 #AU
vx[0] = 0.0 #AU/yr
vy[0] = 8.17 #AU/yr

# Calculate x,y position and velocity for each time in the time array.
for i in range(len(time)-1):
	vx[i+1] = (-G/r[i]**3)*(1+(alpha/r[i]**2))*x[i]*dt + vx[i]
	vy[i+1] = (-G/r[i]**3)*(1+(alpha/r[i]**2))*y[i]*dt + vy[i]
	x[i+1] = vx[i+1]*dt + x[i]
	y[i+1] = vy[i+1]*dt + y[i]
	r[i+1] = (x[i+1]**2 + y[i+1]**2)**0.5


# Plot orbit to ensure results look as predicted (elliptical orbit)

plt.figure()
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.title('Orbit of Mercury with exaggerated affects of general relativity ')
plt.plot(0,0,'o',color = 'DarkOrange',markersize = 8,label = 'The Sun')
plt.plot(x,y)

'''
plt.figure()
plt.subplot(211)
plt.xlabel('time [yr]')
plt.ylabel('x [AU]')
plt.title('Motion of Mercury in x-coordinate over time')
plt.plot(time,x)
plt.subplot(212)
plt.xlabel('time [yr]')
plt.ylabel('y [AU]')
plt.title('Motion of Mercury in y-coordinate over time')
plt.plot(time,y)
plt.suptitle('Orbit of Mercury')
'''
plt.show()



