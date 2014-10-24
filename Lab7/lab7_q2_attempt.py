import numpy as np
import matplotlib.pyplot as plt

a = 1.
b = 3.

def f(r):
	x,y = r
	dxdt = 1-(b+1)*x + a*y*x**2
	dydt = b*x - a*y*x**2
	return np.array([dxdt,dydt])

'''
N = 1.e4
t1 = 0.
t2 = 20.
h = (t2-t1)/N
ts = np.arange(t1,t2+h,h)
## EULER TEST ##
rs = []
r = np.array([0,0])
rs.append(r)
time = t1
while time < t2:
	print r
	r = r + h*f(r)
	time += h
	rs.append(r)

rs = np.array(rs)
'''

def MMM(r,fn,tint,H,n):
	print 'Called modified midpoint method'
	tstart,tend = tint
	h = H/n
	print 'h = ',h
	t = tstart
	x0 = r
	ym = x0 + 0.5*h*fn(x0)
	xm = x0 + h*fn(ym)
	t += h
	print 'x1,y1 = ',xm,ym
	while t < tend:
		ym += h*f(xm)
		xm += h*f(ym)
		if np.isinf(xm[1]) == False:
			print 'xm,ym = ',xm,ym
	xest = 0.5*(xm + ym + 0.5*h*f(xm))
	return xest

def Richardson(Rnm,Rn_1m,n,m):
	print 'Called Richardson extrapolation'
	err = (Rnm - Rn_1m)/((n/(n-1))**(2*m) - 1)
	return Rnm + err, abs(err)

def BSstep():


def BSmeth(r,fn,tint,H,nmax,delta):
	tstart,tend = tint
	acc = delta*H
	rs = []
	rs.append(r)
	ts = []
	ts.append(tstart)
	time = tstart
	while time < tend:
		Rexts = []
		n = 1
		R11 = MMM(r,fn,np.array([time,time+H]),H,n)
		Rexts.append([R11])
		while n < nmax:
			n+=1
			Rs = []
			Rn1 = MMM(r,fn,np.array([time,time+H]),H,n)
			Rs.append(Rn1)
			for j in range(n):
				m = j+1
				Rnm = Rs[j]
				Rn_1m = Rexts[(n-1)-1][j]
				Rnm1,err = Richardson(Rnm,Rn_1m,n,m)
				rval = Rnm1
				Rs.append(Rnm1)
			Rexts.append(Rs)
		if err < acc:
			print 'Finished interval'
			rs.append(rval)
			time += H
			ts.append(time)
		elif err > acc:
			print 'Subdividing'
			r1 = BSmeth(r,fn,tint,H/2.,nmax,delta)
			r2 = BSmeth(r1,fn,tint,H/2.,nmax,delta)
	return np.array(ts),np.array(rs)


x0 = 0.
y0 = 0.
r0 = np.array([x0,y0])
delta = 1e-10
tstart = 0.
tend = 20.
tint = np.array([tstart,tend])
nmax = 8
H = 20.

time,posvec = BSmeth(r0,f,tint,H,nmax,delta)

plt.plot(time,posvec[:,0])
plt.plot(time,posvec[:,1])



