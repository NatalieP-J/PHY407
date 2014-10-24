from numpy import array,arange,append

# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
N = 1000
V0 = 50. * e
a = 1e-11
x0 = -10*a
x1 = 10*a
L = x1-x0
h = L/N

# Potential function
def V(x):
    return V0*(x/a)**4

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi,fphi],float)

# Calculate the wavefunction for a particular energy
def solve(E):
    psi = 0.0
    phi = 1.0
    r = array([psi,phi],float)

    for x in arange(x0,x1,h):
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6.

    return r[0]

def secant(Ebracket,psi2,target):
    E1,E2 = Ebracket
    while abs(E1-E2)>target:
        psi1,psi2 = psi2,solve(E2)
        E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)
    return E2

# Main program to find the energy using the secant method
eigenenergies = array([])

target = e/1000

E1 = 0.0
E2 = e

psi2 = solve(E1)

E2 = secant([E1,E2],psi2,target)

eigenenergies = append(eigenenergies,E2)

E1 = 1.5*E2
E2 *= 2

psi2 = solve(E1)

E2 = secant([E1,E2],psi2,target)

eigenenergies = append(eigenenergies,E2)

E1 = 1.5*E2
E2 *= 1.8

psi2 = solve(E1)

E2 = secant([E1,E2],psi2,target)

eigenenergies = append(eigenenergies,E2)
