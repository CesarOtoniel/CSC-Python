"""
Program: shiftleft.py
Author: Cesar Guevara

Problem:A bit shift is a procedure whereby the bits
 in a bit string are moved to the left or the right. 
For example, we can shift the bits in string 1011 two 
places to the left to produce string 1110. Note that 
the leftmost two bits are wrapped 

around the right side of the string in this operation. 
Define two scripts, shift-left .py and shiftRight.py, 
which expects a bit string as an input. The script
shiftLeft shifts the bits in its input one place to 
the left, wrapping the leftmost bit to the rightmost 
position.

The script shiftRight performs the inverse operation.
Each script prints the resulting string.

1. Significant constants:
	none
2. The inputs are:
	ring	##string to shift around
3. Computations:
	
4. The outputs are:
	ring
"""

# Initialize the constants

# Request inputs
ring = str(input("Insert a string to shift: "))
shifts = int(input("Insert a number of times to shift: "))

# Computations
if len(ring)>=shifts:
	shifts=shifts%len(ring)
output=""

for ch in range(len(ring)):
	if(ch<len(ring)-shifts):
		output=output+ring[ch+shifts]
for ch in range(shifts):
	output=output+ring[ch]
print(output)
# Display results
