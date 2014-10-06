import numpy as np
import matplotlib.pyplot as plt

sigma = 25.
eps = 10**-3

blur = np.loadtxt('blur.txt')

def gauss2D(rows,cols,sigma):
	gauss = np.zeros((rows,cols))
	for i in range(rows):
		ip = i
		if ip > rows/2:
			ip -= rows
		for j in range(cols):
			jp = j
			if jp > cols/2:
				jp -= cols
			gauss[i][j] = np.exp(-(ip**2 + jp**2)/(2.*sigma**2))
	return gauss

rows = len(blur)
cols = len(blur[0])

psf = gauss2D(rows,cols,sigma)

fblur = np.fft.rfft(blur)
fpsf = np.fft.rfft(psf)

funblur = np.zeros(fblur.shape,complex)

ilist = []
for i in range(len(fpsf)):
	for j in range(len(fpsf[i])):
		if abs(fpsf[i][j]) >= eps:
			ilist.append((i,j))
			funblur[i][j] = fblur[i][j]/fpsf[i][j]
		elif abs(fpsf[i][j]) < eps:
			funblur[i][j] = fblur[i][j]

unblur = np.fft.irfft(funblur/(rows*cols))

plt.gray()
plt.figure()
plt.imshow(unblur,vmax = 0.001)
plt.show()
