"""
Program: GCD.py
Author: Cesar Guevara


1. Significant constants:

2. The inputs are:
	numbera
	numberb
3. Computations:
	lesserNumber
	gcd
4. The outputs are:
	gcd
"""

# Initialize the constants

# Request inputs
numbera=int(input("Please instert first number: "))
numberb=int(input("Please insert second number: "))

# Computations
if (numbera <  numberb):
	lesserNumber=numbera
	greaterNumber=numberb
else:
	lesserNumber=numberb
	greaterNumber=numbera

if (lesserNumber==0):
        if(greaterNumber%2==1):
            print(1)
        else:
            print(2)

for gcd in range(lesserNumber,0,-1):
	if(greaterNumber%gcd==0 and lesserNumber%gcd==0):
		print(f"{gcd}")
		break
# Display results
