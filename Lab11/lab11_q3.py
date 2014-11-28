from numpy import arange,array,where,copy,exp,log,mod
from random import randrange,random
import matplotlib.pyplot as plt
from time import sleep
plt.ion()

###############################################################################

# This code finds the minimum energy distribution of two state (up or down) 
# dipoles in a Ising model grid. It does this by repeatedly randomly flipping
# the spin of one of the dipoles and calculating the energy of each 
# configuration. Lower energy configuration are always accepted, while higher
# energy configurations are accepted with probability governed by the Boltzmann
# distribution.

################################## CONSTANTS ##################################

animate = False # Switch to toggle animation
T0 = 10. # Initial temperature for cooling schedule
Tmin = 1.e-4 # Final temperature for cooling schedule
tau = 1e5 # Cooling rate
kb = 1 # Boltzmann constant
L = 50 # Square grid side length

################################## FUNCTIONS ##################################

# Given a point x,y this function chooses on of the four adjacent points on a 
# 2D grid
def adjacentpt(x,y):
    z = randrange(0,4)
    if z == 0:
        nx,ny = x,y+1
    if z == 1:
        nx,ny = x,y-1
    if z == 2:
        nx,ny = x+1,y
    if z == 3:
        nx,ny = x-1,y
    if nx < 0 or ny < 0 or nx >= L or ny >= L:
        nx,ny = adjacentpt(x,y)
    return nx,ny

# A function to find the 'energy' we wish to minimize. Since we awant to maximize
# the number of dimers, we want to minimize negative the number of dimers
def energy(dimerlist):
    return -len(dimerlist)

# Metropolis acceptance probability determinant
def metro_accept(E1,E2,T):
    if E2 <= E1: # If we are in lower energy state than previous, return True
        return True
    elif E2 > E1: # If we are in higher energy state than previous
        beta = 1./(kb*T)
        P = exp(-beta*(E2-E1))
        z = random()
        if z <= P: # Return True if a random number is less than the probability
            return True
        elif z > P: # Return False if a random number is greater than the probability
            return False

# A function describing the rate of the cooling schedule
def temperature(t):
    return T0*exp(-t/float(tau))

################################## MAIN PROGRAM ##################################

# List of dimer locations (pairs of points)
dimer = []
# List of empty points (single points)
empty = []
# Fill the empty points list with each point, initially
for l1 in range(L):
    for l2 in range(L):
        empty.append([l1,l2])

# List to hold energy of each configuration
energies = []

# If animation switch is active, animate the dimer covering process
if animate == True:
    plt.figure()
    ax = plt.axes(xlim = (-0.5,L-0.5),ylim = (-0.5,L-0.5))
    ax.vlines(arange(-1,L+1)+0.5,-0.5,L+0.5)
    ax.hlines(arange(-1,L+1)+0.5,-0.5,L+0.5)

energies.append(energy(dimer))

# Create variable to track the number of timesteps
i = 0
# Set initial temperature
T = T0
# Calculate the total amount of timesteps needed to get to the minimum 
# temperatuure
totaltime = -tau*log(Tmin/T0)
while T > Tmin:
    # Print status update every 10000 steps
    if mod(i,10000) == 0:
        print 'i = ',i, 'of', int(totaltime)
    # Make copies of the dimer and empty lists to make our potential change
    # These arrays will be reset if the state is not accepted
    dtemp = list(dimer)
    etemp = list(empty)
    # Calculate the temperature
    T = temperature(float(i))
    # Find a random point
    x1 = randrange(0,L)
    y1 = randrange(0,L)
    # Choose an adjacent point
    x2,y2 = adjacentpt(x1,y1)
    # If both points are unoccupied, put a dimer there
    if [x2,y2] in empty and [x1,y1] in empty:
        if animate == True:
            ax.plot([x1,x2],[y1,y2],'-o',color = 'b')
            plt.draw()
        dtemp.append([[x1,y1],[x2,y2]]) # Add dimer location
        # Remove the two points from the list of empty points
        etemp.remove([x1,y1])
        etemp.remove([x2,y2])
    # If the pair of points is occupied, remove the dimer
    elif [[x1,y1],[x2,y2]] in dimer:
        if animate == True:
            k = dimer.index([[x1,y1],[x2,y2]])
            ax.lines.pop(k)
            plt.draw()
        dtemp.remove([[x1,y1],[x2,y2]]) # Remove the dimer location
        # Add both points to the list of empty arrays
        etemp.append([x1,y1])
        etemp.append([x2,y2])
    elif [[x2,y2],[x1,y1]] in dimer:
        if animate == True:
            k = dimer.index([[x2,y2],[x1,y1]])
            ax.lines.pop(k)
            plt.draw()
        dtemp.remove([[x2,y2],[x1,y1]]) # Remove the dimer location
        # Add both points to the list of empty arrays
        etemp.append([x1,y1])
        etemp.append([x2,y2])
    # Calculate the energy of the new dimer configuration
    enew = energy(dtemp)
    # Determine whether the new configuration is accepted
    accept = metro_accept(energies[-1],enew,T)
    # If the new configuration is accepted, update the dimer and empty list
    if accept == True:
        energies.append(enew)
        dimer = list(dtemp)
        empty = list(etemp)
    i+=1

################################## PLOT ##################################

plt.figure()
ax = plt.axes(xlim = (-0.5,L-0.5),ylim = (-0.5,L-0.5))
ax.vlines(arange(-1,L+1)+0.5,-0.5,L+0.5)
ax.hlines(arange(-1,L+1)+0.5,-0.5,L+0.5)
for i in range(len(dimer)):
    d = array(dimer[i])
    ax.plot(d[:,0],d[:,1],'-o',color = 'b')
plt.title('Dimer coverage for tau = {0}'.format(tau))
fig = plt.gca()
fig.axes.get_xaxis().set_ticks([])
fig.axes.get_yaxis().set_ticks([])


