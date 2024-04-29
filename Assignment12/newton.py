"""
Program: newton.py
Author: Cesar Guevara

For problems 6.1 and 6.2

Package Newton’s method for approximating square roots (Case Study 3-2) 
in a function named newton . This function expects the input number as 
an argument and returns the estimate of its square root. The script in 
the file named newton.py should also include a main function that allows 
the user to compute square roots of inputs until she presses the 
enter/return key. (LO: 6.2)

Restructure Newton’s method (Case Study 3-2) by decomposing it into three 
cooperating functions. The task of testing for the limit is assigned to a 
function named limitReached , whereas the task of computing a new 
approximation is assigned to a function named improveEstimate . Each 
function, in the file named newton.py, expects the relevant arguments and 
returns an appropriate value. (LO: 6.2)



1. Significant constants:
	tolerance
	estimate
2. The inputs are:
	number
3. Computations:
	difference
	tolerance
	number
4. The outputs are:
	number
"""
# Import libraries
import math


def newton():
	while True:
#Initialize constants
		tolerance = 0.000001
		estimate = 1.0
#Ask for user Input
		number = input("Enter a positive number: ")
		if number == '':
			break
		number = float(number)
# Computations
		while True:
			estimate=improveEstimate(estimate,tolerance,number)
			if limitReached(estimate,tolerance,number):
				break
#Display results
		print("Th eprogram's estimate:",estimate)
		print("Python's estimate:	",math.sqrt(number))

def limitReached(estimate, tolerance,number):
	difference = abs(number-estimate**2)
	if difference <= tolerance:
		return True
	else:
		return False

def improveEstimate(estimate,tolerance,number):
	estimate=(estimate+ number /estimate)/2
	return estimate

if __name__ == '__main__':
	newton()



