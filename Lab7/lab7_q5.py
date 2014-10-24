from numpy import array,arange,append
import matplotlib.pyplot as plt

###############################################################################

# This code calculates the first three energy eigenvalues of a square well with 
# an anharmonic oscillator potential and prints the results. It does this by
# finding the energy corresponding to a wave function with zeros at each side of 
# the well. This is determined by employing the secant method and integrating 
# Schrodinger's equation to find the wave function.

################################## CONSTANTS ##################################

m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
N = 1000           # Number of steps across the x-range 
V0 = 50. * e       # Potential constant for the potential function
a = 1e-11          # Length scale for the potential function
x0 = -10*a         # Bounds the well
x1 = 10*a
L = x1-x0
h = L/N            # Size of integration steps
xs = arange(x0/2.,x1/2.,h/2.)

################################## FUNCTIONS ################################## 

# Potential function
def V(x):
    return V0*(x/a)**4

# Schrodinger's equation divided into two first order ODEs
def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi,fphi],float)

# Calculate the wavefunction for a particular energy using fourth order
# Runge-Kutta and initial conditions psi = 0 and dpsi/dx = phi = 1
def solve(E,x0,x1,h):
    psi = 0.0
    phi = 1.0
    r = array([psi,phi],float)
    psivals = []
    for x in arange(x0,x1,h):
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6.
        psivals.append(r[0])

    return r[0], array([psivals])

# Secant method for finding zeros 
def secant(Ebracket,target,x0,x1,h):
    E1,E2 = Ebracket
    psi2 = solve(E1,x0,x1,h)[0]
    while abs(E1-E2)>target:
        psi1,psi2 = psi2,solve(E2,x0,x1,h)[0]
        E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)
    return E2

# Simpson's Rule integration for a discrete set of points
def simpsons(pts):
    N = len(pts)
    s = pts[0] + pts[-1]
    for k in range(1,N,2):
        s += 4*pts[k]
    for k in range(2,N-1,2):
        s += 2*pts[k]
    return s

################################## MAIN PROGRAM ################################## 
# Inclued eigenvalues for energy as computed in lab7_q4
eigenenergies = array([205.30690346,735.691247041,1443.56942133])*e

# Find the wave functions for each energy eigenvalue
psig = solve(eigenenergies[0],x0/2.,x1/2.,h/2.)[1][0]
psi1 = solve(eigenenergies[1],x0/2.,x1/2.,h/2.)[1][0]
psi2 = solve(eigenenergies[2],x0/2.,x1/2.,h/2.)[1][0]

# Find the normalization constant for each constant
psigsq = (2*simpsons(abs(psig[:len(psig)/2])**2))**0.5
psi1sq = (2*simpsons(abs(psi1[:len(psi1)/2])**2))**0.5
psi2sq = (2*simpsons(abs(psi2[:len(psi2)/2])**2))**0.5

################################## PLOT ################################## 

plt.figure()
plt.plot(xs,psig/psigsq,label = 'Ground State')
plt.plot(xs,psi1/psi1sq,label = 'First Excited State')
plt.plot(xs,psi2/psi2sq,label = 'Second Excited State')
plt.xlabel('$x$ [$m$]')
plt.ylabel('Normalized $\psi (x)$ [$m^{-1/2}$]')
plt.title('Eigenstates of the Square Well with an Anharmonic Oscillator Potential')
plt.legend(loc = 'best')
plt.xlim(-5*a,5*a)
plt.show()

