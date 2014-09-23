import numpy as np
import matplotlib.pyplot as plt

phi = np.pi/4.
h1 = 2.5
h2 = 2*h1

def inten(dwdx,dwdy):
	num = np.cos(phi)*dwdx + np.sin(phi)*dwdy
	den = np.sqrt((dwdx**2) + (dwdy**2) + 1)
	return num/den

alt = np.loadtxt('stm.txt')
altT = np.transpose(alt)

dwdx = np.zeros(alt.shape)
dwdy = np.zeros(altT.shape)

for i in range(len(alt)):
	for k in range(len(alt[i])):
		if k == 0:
			dwdx[i][k] = (alt[i][k+1] - alt[i][k])/h1
		if k == (alt.shape[1] - 1):
			dwdx[i][k] = (alt[i][k] - alt[i][k-1])/h1
		else:
			dwdx[i][k] = (alt[i][k+1] - alt[i][k-1])/h2


for i in range(len(altT)):
	for k in range(len(altT[i])):
		if k == 0:
			dwdy[i][k] = (altT[i][k+1] - altT[i][k])/h1
		if k == (altT.shape[1] - 1):
			dwdy[i][k] = (altT[i][k] - altT[i][k-1])/h1
		else:
			dwdy[i][k] = (altT[i][k+1] - altT[i][k-1])/h2

dwdy = np.transpose(dwdy)

I = inten(dwdx,dwdy)

plt.gray()
plt.axis('off')
plt.title('Intensity of light on the surface of silicon for a striking angle of 45 degrees')
plt.imshow(I,vmax = 0.3, vmin = -0.3)