"""
Program: encrypt.py
Author: Cesar Guevara
Use the strategy of the decimal to binary conversion 
and the bit shift left operation defined in Programming
 Exercise 5 to code a new encryption algorithm in the 
file encrypt.py. The algorithm should add 1 to each 
character’s numeric ASCII value, convert it to a bit 
string, and shift the bits of this string one place 
to the left. A single-space character in the encrypted 
string separates the resulting bit strings.

1. Significant contants:

	none

2. The inputs are:

	plainText #Text to be encoded 
	
	distance  #distance beetween the value of 
		  #ord() of the encrypted and 
		  #unencrypted letter 

3. Computations:

	cipherValue #new ord() value in ciphered character

4. The outputs are:
	code        #string with all the ciphered values
"""

# Initialize the constants

# Request inputs
file = input("Enter the file name: ")
distance = int(input("Enter the distance value: "))
code = ""
# Computations
file = open(file,'r')
plainText =file.read()
for ch in plainText:
	ordValue=ord(ch)
	cipherValue = ordValue+distance
	if cipherValue > 127:
		cipherValue = distance - (127 - ordValue +1)
	code += chr(cipherValue)
# Display results/Write results to a file

outputFile=open("Encrypted.txt",'w')
outputFile.write(code)
outputFile.close() 

