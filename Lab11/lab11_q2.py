import numpy as np
from random import random,randrange
import matplotlib.pyplot as plt
plt.ion()

###############################################################################

# This code finds the minimum energy distribution of two state (up or down) 
# dipoles in a Ising model grid. It does this by repeatedly randomly flipping
# the spin of one of the dipoles and calculating the energy of each 
# configuration. Lower energy configuration are always accepted, while higher
# energy configurations are accepted with probability governed by the Boltzmann
# distribution. The dipoles are animated as they change

################################## CONSTANTS ##################################

animate = False # Animation toggle
J = 1 # Constant scalar multiple for energy with units of energy
T = 3. # Temperature: arbitrary units
kb = 1 # Boltzmann constant, arbitrary units
beta = 1./(T*kb) # A consolidating constant used in the energy calculation
ndip = 20 # Number of dipoles
niter = int(1e6) # Number of iterations

################################## FUNCTIONS ##################################

# Calculate the energy of 2D array of two state dipoles
def energy(ss):
    lr = (ss.T[0:-1]).T*(ss.T[1:]).T
    ud = ss[0:-1]*ss[1:]
    return -J*(np.sum(lr) + np.sum(ud))

# Calculate the magnetization of an array of two state dipoles
def magnet(ss):
    return np.sum(ss)

# Metropolis acceptance probability determinant
def metro_accept(E1,E2):
    if E2 <= E1: # If we are in lower energy state than previous, return True
        return True
    elif E2 > E1: # If we are in higher energy state than previous
        P = np.exp(-beta*(E2-E1))
        z = random()
        if z <= P: # Return True if a random number is less than the probability
            return True
        elif z > P: # Return False if a random number is greater than the probability
            return False

################################## MAIN PROGRAM ################################## 

# Initialize initial array of dipoles
ss = np.random.randint(0,2,(ndip,ndip))
ss[np.where(ss==0)] = -1

if animate == True:
    # Set up animation
    plt.figure()
    # Choose axes
    ax = plt.axes(xlim = (-0.5,ndip-0.5),ylim = (-0.5,ndip-0.5))
    # Create grid
    ax.vlines(np.arange(-1,ndip+1)+0.5,-0.5,ndip+0.5)
    ax.hlines(np.arange(-1,ndip+1)+0.5,-0.5,ndip+0.5)
    # Plot up dipoles
    ax.plot(np.where(ss==1)[0],np.where(ss==1)[1],'r^',markersize = 10)
    # Plot down dipoles
    ax.plot(np.where(ss==-1)[0],np.where(ss==-1)[1],'bv',markersize = 10)
    plt.title('Temperature = {0}'.format(T))
    # Turn off axis labels
    fig = plt.gca()
    fig.axes.get_xaxis().set_ticks([])
    fig.axes.get_yaxis().set_ticks([])
    plt.draw()

# Create empty arrays to hold energy and magnetization at each step
energies = []
magnets = []

# Add the energy and magnetization of the initial configuration
energies.append(energy(ss))
magnets.append(magnet(ss))

for i in range(niter):
    # Print status update every 10000 steps
    if np.mod(i,10000) == 0:
        print 'i = ',i, 'of', niter
    newss = np.copy(ss)
    # Choose a random position in the array
    x,y = randrange(0,ndip),randrange(0,ndip)
    # Flip the spin of the dipole at the random position
    newss[x][y] *= -1
    # Calculate the energy of the new state
    enew = energy(newss)
    # Determine whether or not the new state is accepted
    accept = metro_accept(energies[-1],enew)
    # If the new state is accepted, add its details to appropriate lists
    if accept == True:
        ss = newss
        energies.append(enew)
        magnets.append(magnet(newss))
        if animate == True:
            ax.lines.pop(-1)
            ax.lines.pop(-1)
            ax.plot(np.where(ss==1)[0],np.where(ss==1)[1],'r^',markersize = 10)
            ax.plot(np.where(ss==-1)[0],np.where(ss==-1)[1],'bv',markersize = 10)
            plt.draw()

################################## PLOT ################################## 

plt.figure()
# Choose axes
ax = plt.axes(xlim = (-0.5,ndip-0.5),ylim = (-0.5,ndip-0.5))
# Create grid
ax.vlines(np.arange(-1,ndip+1)+0.5,-0.5,ndip+0.5)
ax.hlines(np.arange(-1,ndip+1)+0.5,-0.5,ndip+0.5)
# Plot up dipoles
ax.plot(np.where(ss==1)[0],np.where(ss==1)[1],'r^',markersize = 10)
# Plot down dipoles
ax.plot(np.where(ss==-1)[0],np.where(ss==-1)[1],'bv',markersize = 10)
plt.title('Temperature = {0}'.format(T))
# Turn off axis labels
fig = plt.gca()
fig.axes.get_xaxis().set_ticks([])
fig.axes.get_yaxis().set_ticks([])
plt.draw()

plt.figure()
plt.subplot(211)
plt.plot(energies)
plt.ylabel('Energy')
plt.title('Energy and magnetization of a Ising magnetic dipole model after 1 million Monte Carlo steps')
plt.subplot(212)
plt.plot(magnets)
plt.xlabel('Step Number')
plt.ylabel('Magnetization')
