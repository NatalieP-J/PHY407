from numpy import array,arange,append

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

# Secant method for finding zeros 
def secant(Ebracket,target):
    E1,E2 = Ebracket
    psi2 = solve(E1)
    while abs(E1-E2)>target:
        psi1,psi2 = psi2,solve(E2)
        E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)
    return E2

################################## MAIN PROGRAM ################################## 
# Create array to hold results
eigenenergies = array([])

# Specify target accuracy
target = e/1000

# Guess at energies that bracket the ground state energy
E1 = 0.0
E2 = e

psi2 = solve(E1)

# Solve for ground state energy
E2 = secant([E1,E2],target)
eigenenergies = append(eigenenergies,E2)

# Guess at energies that bracket the first excited state energy
E1 = 3*E2
E2 *= 2

# Solve for first excited state energy
E2 = secant([E1,E2],target)
eigenenergies = append(eigenenergies,E2)

# Guess at energies that bracket the second excited state energy
E1 = 1.3*E2
E2 *= 1.7

# Solve for the second excited state energy
E2 = secant([E1,E2],target)
eigenenergies = append(eigenenergies,E2)

# Print resulting eigenvalues
print 'Value accuracy = ',target/e,'eV'
print 'Ground State Energy =',eigenenergies[0]/e,'eV'
print 'First Excited State Energy =',eigenenergies[1]/e,'eV'
print 'Change in energy =  ', eigenenergies[1]/e - eigenenergies[0]/e,'eV'
print 'Second Excited State Energy =',eigenenergies[2]/e,'eV'
print 'Change in energy =  ', eigenenergies[2]/e - eigenenergies[1]/e,'eV'


