"""
Program: salary.py
Author: Cesar Guevara

Compute a school district's salary schedule.

1. Significant constants:

2. The inputs are:

   starting salary
   annual percentage increase
   number of years for which to print the schedule
   starting year

3. Computations:

    salary
    newSalary

4. The outputs are:

    Two columns containing the year and the salary
    after the increase.
"""

# Initialize the constants

# Request inputs
startingSalary= float(input("Insert starting salary: "))
increasePerYear= float(input("Insert the annual percentage increase: "))
numberOfRows=int(input("Number of years to calculate: "))
# Computations

# Display results
year=1
print("%-4d %10.2f" % (year, startingSalary))

for year in range(2, numberOfRows + 1):
    newSalary = startingSalary + startingSalary*(increasePerYear/100)
    startingSalary = newSalary
    print("%-4d %10.2f" % (year, newSalary))
