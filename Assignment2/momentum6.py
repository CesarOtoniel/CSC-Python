"""
Program: momentum6.py
Author: Cesar Guevara

Calculates momentum using mass in kg and velocity in m/s as an input.
This version also calculates teh kineticEnergy of the same object with the same variables.

1. Significant constants
	NULL	
2. The inputs are:
	mass (in kg)
	velocity(m/s)
3. Computations:
	momentum = mass * velocity
	kineticEnergy = mass * velocity**2
4. The outputs are:
	momentum (in kg*m.s)
	kineticEnergy = mass * velocity**2 /2
"""

# Initialize the constants

# Request inputs
mass = float(input("Please insert the mass of the object in kg: "))
velocity = float(input("Please insert the velocity of such object with {mass} kg of mass in m/s: "))
# Computations
momentum = mass*velocity
kineticEnergy = mass * velocity ** 2/2
# Display results
print(f"The momentum of such object with mass of {mass} kg and velocity of {velocity} m/s is: {momentum} kg*m/s")
print(f"Its Kinetic energy on the other hand is {kineticEnergy} kg * m^2 / s^2")
