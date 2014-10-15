import numpy as np
import matplotlib.pyplot as plt

###############################################################################

# This program finds the discrete Fourier transform of a set of data, then discards
# all but the first 2% of coefficients to approximate the data

################################## LOAD DATA ##################################

dow = np.loadtxt('dow2.txt')

################################## MAIN PROGRAM ##################################

cks = np.fft.rfft(dow)

percent_discard = 0.02
ind = int(percent_discard*len(cks))

cks_new = np.concatenate((cks[:ind],np.zeros(len(cks) - ind)))

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