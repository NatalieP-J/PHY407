from gaussint import gaussint
import numpy as np
import matplotlib.pyplot as plt

# This code computes the heat capacity for a block of aluminum for temperature
# range from 5K to 500K and plots the result. This code prints status updates
# during this computation on line 59. 


# Set constants needed for the program

# Volume of sample
V = 1000. #cm^3
V /= 100.**3 #m^3
# Number density of sample
rho = 6.022e28 #m^-3
# Boltzmann constant (rounded to 4 sig figs)
kb = 1.381e-23 #m^2 kg s^-2 K^-1
# Debye temperature
Dt = 428. #K
# Number of sample points for Gaussian quadrature
N = 50

# The integrand in the integral in the equation for heat capacity
def Cvintr(x):
	num = x**4*np.exp(x) # numerator
	den = (np.exp(x)-1)**2 # denominator
	return num/den

# The equation for heat capacity
def Cv(T):
	Tratio = T/Dt # ratio of temperature to Debye temperature
	lead = 9*V*rho*kb*(Tratio)**3 # leading term before integral
	a = 0 # lower limit of integral
	b = 1./Tratio # upper limit of integral 
	intg = gaussint(Cvintr,N,a,b)
	return lead*intg

# Create temperature array and array to hold heat capacities
temp = np.arange(5,500,0.5)
C = np.zeros(len(temp))

# Loop through temperatures ancd compute heat capacity for each
for t in range(len(temp)):
	print 'Temperature rising ....... ', temp[t],' K'
	C[t] = Cv(temp[t])

# Plot heat capacity vs temperature
plt.title('Heat capacity of a sample of aluminum with a volume of 1000 $cm^3$')
plt.xlabel('Temperature [K]')
plt.ylabel('Heat capacity [J/K]')
plt.plot(temp,C)
plt.show()
