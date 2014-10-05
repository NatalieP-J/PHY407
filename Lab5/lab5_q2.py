import numpy as np
import matplotlib.pyplot as plt

def f(x):
	fs = []
	for i in range(len(x)):
		if np.mod(int(x[i]),2) == 0:
			fs.append(1)
		elif np.mod(int(x[i]),2) != 0:
			fs.append(-1)
	return fs

N = 1000

n = np.linspace(0,2,N)

cks = np.fft.rfft(f(n))

eject = 10

cks_new = np.concatenate((cks[:eject],np.zeros(N-eject)))

f_new = np.fft.irfft(cks_new)

n_new = np.linspace(0,2,len(f_new))

plt.plot(n,f(n),linewidth = 4)
plt.plot(n_new,f_new/max(f_new),linewidth = 3)
plt.ylim(-2,2)
plt.show()
