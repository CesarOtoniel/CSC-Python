"""
Program: convert.py
Author: Cesar Guevara

Chapter 4 presented an algorithm for converting from binary to decimal.
You can generalize this algorithm to work for a representation in any base.
 Instead of using a power of 2, this time you use a power of the base.
Also, you use digits greater than 9, such as A … F, when they occur.
Define a function named repToDecimal in the file convert.py
that expects two arguments, a string and an integer.
The second argument should be the base. For example,
repToDecimal("10", 8) returns 8, whereas repToDecimal("10", 16) returns 16.
The function should use a lookup table to find the value of any digit
Make sure that this table (it is actually a dictionary) is initialized
before the function is defined. For its keys, use the 10 decimal digits
(all strings) and the letters A … F (all uppercase). The value stored with
each key should be the integer that the digit represents. (The letter 'A'
associates with the integer value 10, and so on.) The main loop of the
function should convert each digit to uppercase, look up its value in
the table, and use this value in the computation. Include a main function
that tests the conversion function with numbers in several bases.

1. Significant constants:
	valDictionary
2. The inputs are:
	numString
	base
3. Computations:
	nBaseN
4. The outputs are:
	nBaseN
5. Functions are:
	repToDecimal(str base, int number)
"""
def repToDecimal(number,base):
	nBaseNumber = 0
	exponent = len(number) - 1
	for char in number:
		digit=valdict[char]
		nBaseNumber = nBaseNumber + digit * base ** exponent
		exponent = exponent - 1
	return nBaseNumber
# Initialize the constants
valdict={}
for i in range(48,58):	#Populates dictionaries with pairs '1':1~'9':9
	valdict[chr(i)] = i-48
for i in range(65,91):
	valdict[chr(i)]= i-55 #Populates dictionary with characters 'A':10~'Z'~'35'
# Request inputs
numString = str(input("Enter a string of numbers: "))
numString = numString.upper() #to avoid an error on lowercase
base = int(input("Enter the base for the number: "))
# Computations
decimal = repToDecimal(numString,base)
# Display results
print(decimal)
