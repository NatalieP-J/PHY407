import numpy as np
import matplotlib.pyplot as plt
from dcst import dct,idct

###############################################################################

# This program finds the discrete cosine transform of a set of data, then discards
# all but the first 2% of coefficients to approximate the data

################################## LOAD DATA ##################################

dow = np.loadtxt('dow2.txt')

################################## MAIN PROGRAM ##################################

# Do discrete cosine transform
cks = dct(dow)

# Choose a percentage of coefficients to discard and find corresponding index
percent_discard = 0.02 # 2%
ind = int(percent_discard*len(cks))

# Create new coefficient array
cks_new = np.concatenate((cks[:ind],np.zeros(len(cks)-ind)))

# Find inverse Fourier transform to determine approximation
dow_new = idct(cks_new)

################################## PLOT ##################################

plt.title('Dow Jones Industrial Average')
plt.xlabel('Day (relative to start day)')
plt.ylabel('Closing value')
plt.plot(dow,label = 'Original data',linewidth = 2)
plt.plot(dow_new,'r',label = 'Smoothed data',linewidth = 2)
plt.xlim(0,len(dow))
plt.legend(loc = 'best')
plt.show()