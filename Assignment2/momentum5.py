"""
Program: momentum5.py
Author: Cesar Guevara

Calculates momentum using mass in kg and velocity in m/s as an input.

1. Significant constants
	NULL	
2. The inputs are:
	mass (in kg)
	velocity(m/s)
3. Computations:
	momentum = mass * velocity
4. The outputs are:
	momentum (in kg*m.s)
"""

# Initialize the constants

# Request inputs
mass = float(input("Please insert the mass of the object in kg: "))
velocity = float(input("Please insert the velocity of such object with {mass} kg of mass in m/s: "))
# Computations
momentum = mass*velocity
# Display results
print(f"The momentum of such object with mass of {mass} kg and velocity of {velocity} m/s is: {momentum} kg*m/s")
