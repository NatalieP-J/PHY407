import numpy as np
import matplotlib.pyplot as plt
from time import clock

###############################################################################

# This code computes the oribit a comet under the influence of solar gravity.
# It does this with fourth order Runga-Kutta solving of Newton's law of
# gravitation for x and y velocity, then uses these results to solve for
# position for adaptive timestep size.

################################## CONSTANTS ##################################

G = 39.5 #AU^3/Msun * yr^2
M = 1. #Msun
AU = 1.496e11 #m
yr = 3600.*24.*365. #s

################################## FUNCTIONS ################################## 

# A function that takes a vector r composed of x and y position and x and y
# velocity, and returns the time derivative of each
def f(r):
    """
    r - a length 4 vector containing x,y,vx and vy in that order
    returns the derivative of each element of r

    """
    x,y,vx,vy = r
    rval = np.sqrt(x**2 + y**2) # magnitude of distance to origin
    dxdt = vx
    dydt = vy
    # x and y componenents of Newton's law of gravitation
    dvxdt = -(G*M/rval**3)*x
    dvydt = -(G*M/rval**3)*y
    return np.array([dxdt,dydt,dvxdt,dvydt])

# A function that completes a single iteration of the fourth order 
# Runge-Kutta ODE solving method
def RK4(h,r,fn):
    """
    h - step size
    r - a length 4 vector containing x,y,vx and vy in that order
    fn - a function that returns the derivative of each element of r

    returns updated version of r 
    """
    k1 = h*fn(r)
    k2 = h*fn(r+0.5*k1)
    k3 = h*fn(r+0.5*k2)
    k4 = h*fn(r+k3)
    return np.array(r+(1./6.)*(k1 + 2*k2 + 2*k3 + k4))

################################## MAIN PROGRAM ##################################

# Set initial conditions if AU and AU/yr
x0 = 4.e12/AU #AU
y0 = 0 #AU
vx0 = 0 #AU/yr
vy0 = (5.e2/AU)*yr #AU/yr

# Choose step size and total integration time
h0 = 0.0005 # yr
hmax = 50.*h0 #yr
totaltime = 100. # yr
delta = 1.e3/AU

# Begin timing the process
start = clock()

# Create output arrays to hold resulting r vectors and errors on x and y position
rs = []
errs = []

# Begin measure of time at zero
time = 0
# Create array to hold timestamps
t = []
t.append(time)

# Create first iteration vector and add it to rs array
r0 = np.array([x0,y0,vx0,vy0])
rs.append(r0)

hs = []
hs.append(h0)
h = h0
# While time integrated up to is less than the total time we wish to integrate
# continue with the next iteration
while time < totaltime:
    # Find the new estimate for position and velocity
    rnew1half= RK4(h,r0,f)
    # To calculate errors, go to time 2h in two ways: by taking another 
    # h-sized step from new estimate, then by taking a 2h-sized step from
    # initial estimate.
    rnew1 = RK4(h,rnew1half,f)
    rnew2 = RK4(2.*h,r0,f)
    # Compute error on x and y according to 8.54, p 359 of Newman
    xerr = (1./30.)*(rnew1[0]-rnew2[0])
    yerr = (1./30.)*(rnew1[1]-rnew2[1])
    # Append the resulting total error to list
    errs.append((xerr**2 + yerr**2)**0.5)
    rho = h*delta/(xerr**2 + yerr**2)**0.5 # 8.53, p 358 of Newman
    # If calculated error was effectively zero (so small that round off error
    # might eliminate it), manually set the step size
    if np.isinf(rho) == True:
        h = hmax
    # if rho > 1, more accuracy than needed for choice of delta
    # move to the next iteration, but increase h according to 
    # 8.52 on p 358 of Newman
    elif rho > 1:
        time += h
        t.append(time)
        hs.append(h)
        r0 = rnew1half
        h *= rho**0.25
        rs.append(rnew1half)
    # if rho < 1, less accuracy than needed for choice of delta
    # stay on this iteration and decrease h according to 8.52
    # on p 358 of Newman
    elif rho < 1:
        h *= rho**0.25

# Stop timing
end = clock()

# Convert list of r vectors into an array
rs = np.array(rs)    

# Create array holding the points in time for which position is now known
t = np.array(t)

print 'Time to run: ', end - start,' s'
print 'Average error: ', np.mean(errs)

################################## PLOT ##################################

plt.figure()
plt.plot(rs[:,0],rs[:,1],'.')
plt.plot(0,0,'y*',markersize = 15) # Mark the Sun's position
plt.xlabel('x [AU]')
plt.ylabel('y [AU]')
plt.title('Orbit of a comet around the sun')

plt.figure()
plt.plot(t,hs)
plt.plot([min(t),max(t)],[h0,h0])
plt.xlim(min(t),max(t))
plt.xlabel('Time [yr]')
plt.ylabel('Step size h [yr]')
plt.title('Evolution of adaptive step size over orbit')
plt.show()