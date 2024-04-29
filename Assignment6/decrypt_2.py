"""
Program: lightyear.py
Author: Cesar Guevara

Problem: Write a script that inputs a line of encrypted 
text and a distance value and outputs plaintext using a 
Caesar cipher. The script should work for any printable 
characters.


1. Significant contants:

	none

2. The inputs are:

	cipherText #Text to be encoded 
	
	distance  #distance beetween the value of 
		  #ord() of the encrypted and 
		  #unencrypted letter 

3. Computations:

	plainText #new ord() value in ciphered character

4. The outputs are:
	decodedMsg #string with all the ciphered values
"""

# Initialize the constants

# Request inputs
cipherFile = input("Enter a message to decrypt: ")
distance = int(input("Enter the distance value: "))
decodedMsg = ""
cipherFile=open(cipherFile,'r')
cipherText=cipherFile.read()
# Computations
for ch in cipherText:
	ordValue=ord(ch)
	cipherValue = ordValue-distance
	if cipherValue > 127:
		cipherValue = distance - (127 - ordValue +1)
	decodedMsg += chr(cipherValue)
# Display results
print(decodedMsg)
