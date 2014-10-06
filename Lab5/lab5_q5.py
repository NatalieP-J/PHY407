import numpy as np
import matplotlib.pyplot as plt

sigma = 25.
eps = 1.e-3

blur = np.loadtxt('blur.txt')

def gauss2D(x,y,sigma):
	result = np.zeros((len(x),len(y)))
	for i in range(len(x)):
		for j in range(len(y)):
			result[i][j] = np.exp(-((x[i]**2 + y[j]**2)/2*sigma**2)) 
	return result

length = np.linspace(0,1,blur.shape[0]/2.)
x = np.concatenate((length,length[::-1]))
y = np.concatenate((length,length[::-1]))

psf = gauss2D(x,y,sigma)

fblur = np.fft.rfft(blur)
fpsf = np.fft.rfft(psf)

funblur = np.zeros(fblur.shape,complex)

geq = np.where(abs(fpsf) >= eps)
les = np.where(abs(fpsf) < eps)

funblur[geq] = fblur[geq]/fpsf[geq]
funblur[les] = fblur[les]

unblur = np.fft.irfft(funblur)

plt.gray()
plt.figure()
plt.imshow(unblur)
plt.show()