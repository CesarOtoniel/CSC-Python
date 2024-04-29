"""
Program: lightyear.py
Author: Cesar Guevara


9. Write a script named numberlines.py. This script creates a program listing from a
source program. This script should prompt the user for the names of two files. The
input filename could be the name of the script itself, but be careful to use a different
output filename! The script copies the lines of text from the input file to the output
file, numbering each line as it goes. The line numbers should be right-justified in
4 columns, so that the format of a line in the output file looks like this example:
1> This is the first line of text. 


1. Significant constants:

	None

2. The inputs are:
	
	firstFile
	secondFile

3. Computations:

	lineNumber

4. The outputs are:

	the script returns no values but prints to terminal
"""

# Initialize the constants

# Request inputs

firstFile=input("Insert the name of the first file:")
secondFile=input("Insert the name of the second file:")
# Computations
firstFile=open(firstFile,'r')
secondFile=open(secondFile,'w')
lineNumber = 1
for line in firstFile:
	lineNumber+=1
	secondFile.write("%4s%1s%s" % (lineNumber,'>', line))
# Display results
