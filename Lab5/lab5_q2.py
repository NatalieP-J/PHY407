import numpy as np
import matplotlib.pyplot as plt

def f(x):
	fs = []
	for i in range(len(x)):
		if np.mod(np.floor(2*x[i]),2) == 0:
			fs.append(1)
		elif np.mod(np.floor(2*x[i]),2) != 0:
			fs.append(-1)
	return fs

N = 1000

n = np.linspace(0,1,N)

cks = np.fft.rfft(f(n))

eject = 10

cks[eject:] = 0

f_new = np.fft.irfft(cks)

n_new = np.linspace(0,1,len(f_new))

plt.plot(n,f(n),linewidth = 4,label = 'Original Function')
plt.plot(n_new,f_new,linewidth = 3,label = '10 Coeffecient Fourier Series')
plt.title('Fourier Transform of a Square Wave')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(-2,2)
plt.legend(loc = 'best')
plt.show()
