"""
Program: lightyear.py
Author: Cesar Guevara
Problem:Write a script that inputs a line of plaintext 
and a distance value and outputs an encrypted text using 
a Caesar cipher. The script should work for any printable
characters.

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
plainText = input("Enter a message: ")
distance = int(input("Enter the distance value: "))
code = ""
# Computations
for ch in plainText:
	ordValue=ord(ch)
	cipherValue = ordValue+distance
	if cipherValue > 127:
		cipherValue = distance - (127 - ordValue +1)
	code += chr(cipherValue)
# Display results
print(code)
