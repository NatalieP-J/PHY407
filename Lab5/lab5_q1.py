import numpy as np
import matplotlib.pyplot as plt

###############################################################################

# This code approximates a complicated set of discrete data with the inverse of 
# its Fourier transform with all but the first ten percent of coefficients
# removed.

################################## LOAD DATA ##################################

dow = np.loadtxt('dow.txt')

################################## MAIN PROGRAM ##################################

# Fourrier transform
cks = np.fft.rfft(dow)

# Decide on an amount to discard and calculate the corresponding index
percent_discard = 0.1 # 10%
ind = int(0.1*len(cks))

# Create new set of Fourier coefficients by discarding all past index ind
cks_new = np.concatenate((cks[:ind],np.zeros(len(cks)-ind)))

# Inverse Fourier transform these new coefficients to find approximation
dow_new = np.fft.irfft(cks_new)

################################## PLOT ##################################
plt.title('Dow Jones Industrial Average')
plt.xlabel('Day (relative to start day)')
plt.ylabel('Closing value')
plt.plot(dow,label = 'Original data',linewidth = 2)
plt.plot(dow_new,'r',label = 'Smoothed data',linewidth = 2)
plt.xlim(0,len(dow))
plt.legend(loc = 'best')
plt.show()