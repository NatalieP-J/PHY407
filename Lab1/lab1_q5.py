from numpy import *
import matplotlib.pyplot as plt

# This code finds the orbit of Mercury under the Sun's gravity for one 
# Earth year with set initial conditions. All distance units are AU, 
# all mass units are Msun and all time units are years.

# Set the gravitational constant in astronomical units, years and the 
# mass of the sun.
G = 39.5 #AU^3/Ms*yr

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
	vx[i+1] = (-G*x[i]/r[i]**3)*dt + vx[i] # update x velocity
	vy[i+1] = (-G*y[i]/r[i]**3)*dt + vy[i] # update y velocity
	x[i+1] = vx[i+1]*dt + x[i] # update x position
	y[i+1] = vy[i+1]*dt + y[i] # update y position
	r[i+1] = (x[i+1]**2 + y[i+1]**2)**0.5 # update separation 

# Plot orbit to ensure results look as predicted (elliptical orbit)
plt.figure()
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.title('Orbit of Mercury')
plt.plot(0,0,'o',color = 'DarkOrange',markersize = 8,label = 'The Sun')
plt.plot(x,y)

# Plot velocity in x and y against time
plt.figure()
plt.subplot(211)
plt.ylabel('v_x [AU/yr]')
plt.plot(time,vx)
plt.subplot(212)
plt.xlabel('time [yr]')
plt.ylabel('v_y [AU/yr]')
plt.plot(time,vy)
plt.suptitle('Velocity of Mercury')

plt.show()



