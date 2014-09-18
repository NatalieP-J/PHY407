from numpy import *
import matplotlib.pyplot as plt

# This code finds the orbit of the Earth under both the Sun's and Jupiter's gravity
# for ten Earth years with set initial conditions. All distance units are AU, all 
# mass units are Msun and all time units are years.

# Set the gravitational constant in astronomical units, years and the 
# mass of the sun. Set the mass of Jupiter.
G = 39.5 #AU^3/Ms*yr
Mjup = 1 #Msun

# Set start time, end time and the time step.
ti = 0 #yr
tf = 3.9 #yr
dt = 0.0001 #yr

# Create time array.
time = arange(ti,tf,dt)

# Create arrays to hold results for x,y position and velocity over the orbit.
# Arrays for Earth under only the Sun's influence.
xes = zeros(len(time)) # x position
yes = zeros(len(time)) # y position
res = zeros(len(time)) # Earth's separation from the Sun
vxes = zeros(len(time)) # x velocity
vyes = zeros(len(time)) # y velocity

#Arrays for Jupiter under only the Sun's influence
xj = zeros(len(time)) # x position
yj = zeros(len(time)) # y position
rj = zeros(len(time)) # Jupiter's separation from the Sun
vxj = zeros(len(time)) # x velocity
vyj = zeros(len(time)) # y velocity

#Arrays for Earth under the Sun's and Jupiter's influence
xe = zeros(len(time)) # x position
ye = zeros(len(time)) # y position
re = zeros(len(time)) # Earth's separation from the Sun
vxe = zeros(len(time)) # x velocity
vye = zeros(len(time)) # y velocity

rej = zeros(len(time)) # Earth's separation from Jupiter

# Set initial x,y position and velocity
xes[0] = 1.0 #AU
yes[0] = 0.0 #AU
res[0] = (xes[0]**2 + yes[0]**2)**0.5 #AU
vxes[0] = 0.0 #AU/yr
vyes[0] = 6.18 #AU/yr

xj[0] = 5.2 #AU
yj[0] = 0.0 #AU
rj[0] = (xj[0]**2 + yj[0]**2)**0.5 #AU
vxe[0] = 0.0 #AU/yr
vyj[0] = 2.63 #AU/yr

xe[0] = 1.0 #AU
ye[0] = 0.0 #AU
re[0] = (xe[0]**2 + ye[0]**2)**0.5 #AU
vxe[0] = 0.0 #AU/yr
vye[0] = 6.18 #AU/yr

rej[0] = ((xj[0]-xe[0])**2 + (yj[0]-ye[0])**2)**0.5


# Calculate xe,y position and velocity for each time in the time array.
for i in range(len(time)-1):
	vxes[i+1] = (-G/res[i]**3)*xes[i]*dt + vxes[i]
	vyes[i+1] = (-G/res[i]**3)*yes[i]*dt + vyes[i]
	xes[i+1] = vxes[i+1]*dt + xes[i]
	yes[i+1] = vyes[i+1]*dt + yes[i]
	res[i+1] = (xes[i+1]**2 + yes[i+1]**2)**0.5
	vxj[i+1] = (-G/rj[i]**3)*xj[i]*dt + vxj[i]
	vyj[i+1] = (-G/rj[i]**3)*yj[i]*dt + vyj[i]
	xj[i+1] = vxj[i+1]*dt + xj[i]
	yj[i+1] = vyj[i+1]*dt + yj[i]
	rj[i+1] = (xj[i+1]**2 + yj[i+1]**2)**0.5
	vxe[i+1] = (-G*xe[i]/re[i]**3 + G*Mjup*(xj[i]-xe[i])/rej[i]**3)*dt + vxe[i] #x different for each force component! fix this!!!
	vye[i+1] = (-G*ye[i]/re[i]**3 + G*Mjup*(yj[i]-ye[i])/rej[i]**3)*dt + vye[i] #also needs to be fixed in q7
	xe[i+1] = vxe[i+1]*dt + xe[i]
	ye[i+1] = vye[i+1]*dt + ye[i]
	re[i+1] = (xe[i+1]**2 + ye[i+1]**2)**0.5
	rej[i+1] = ((xj[i+1]-xe[i+1])**2 + (yj[i+1]-ye[i+1])**2)**0.5


plt.figure()
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.title('Orbit of the Earth and Jupiter over {0} Earth years'.format(tf))
plt.plot(xes,yes,label = 'Earth\'s orbit due to solar gravity')
plt.plot(xe,ye,label = 'Earth\'s orbit due to solar and Jovian gravity')
plt.plot(xj,yj,label = 'Jupiter\'s orbit due to solar gravity')
plt.plot(0,0,'o',color = 'DarkOrange',markersize = 8,label = 'The Sun')
plt.legend(loc = 'lower right')



