"""
Program: lightyear.py
Author: Cesar Guevara

1. Significant constants:
	speedOfLight=3*10**8
2. The inputs are:
	years
3. Computations:
	distancetraveled
4. The outputs are:
	distance traveled (meters)
"""

# Initialize the constants
speedOfLight=int(3*10**8)
# Request inputs
print(1)
years=1
#years=float(input())
# Computations
speedOfLight=float(3*10**8*365 * 24 * 60 ** 2*years)
# Display results
print(f"You have traveled {speedOfLight} meters")
