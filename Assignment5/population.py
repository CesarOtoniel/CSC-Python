"""
Program: population.py
Author: Cesar Guevara

Predict population growth, assuming that no
organisms die.

1. Significant constants:
2. The inputs are:
   the initial number of organisms
   rate of growth (a float > 1)
   the number of hours to achieve the rate
   number of hours of growth

3. Computations:
	    totalPopulation = initialOrganisms*rateOfGrowth/hoursToGrow*numberOfHours
4. The outputs are:
    Total population in int format
"""

# Initialize the constants
# Request inputs
initialOrganisms= float(input("Insert the initial number of organisms: "))
rateOfGrowth= float(input(f"{initialOrganisms}Please insert the rate of growth: "))
hoursToGrow= float(input(f"Please insert the number of hours to achieve {rateOfGrowth} times the population: "))
numberOfHours= float(input(f"{hoursToGrow}How many hours will the population grow for?: "))
# Computations
totalPopulation= float(initialOrganisms)+float(initialOrganisms)*float(rateOfGrowth)/hoursToGrow*float(numberOfHours)
# Display results
print(int(totalPopulation))
