"""
Program: klickstonautsr.py
Author: Cesar Guevara

1. Significant constants:

2. The inputs are:
	kmdistance
3. Computations:
	nauticalmiles=
	km=1/10 000 * 90 * 60
4. The outputs are:
	"{kmdistance} is {nauticalMiles} nautical Miles"
"""

# Initialize the constants

# Request inputs
kmdistance = float(input("Please insert the number of kilometers: "))
# Computations
nauticalMiles= kmdistance*90*60/10000.0
# Display results
print(f"{nauticalMiles} nautical Miles")
