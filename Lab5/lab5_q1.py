import numpy as np
import matplotlib.pyplot as plt

dow = np.loadtxt('dow.txt')

cks = np.fft.rfft(dow)

cks_new = np.concatenate((cks[:int(0.1*len(cks))],np.zeros(len(cks) - int(0.1*len(cks)))))

dow_new = np.fft.irfft(cks_new)

plt.title('Dow Jones Industrial Average')
plt.xlabel('Day (relative to start day)')
plt.ylabel('Closing value')
plt.plot(dow,label = 'Original data',linewidth = 2)
plt.plot(dow_new,'r',label = 'Smoothed data',linewidth = 2)
plt.xlim(0,len(dow))
plt.legend(loc = 'best')
plt.show()