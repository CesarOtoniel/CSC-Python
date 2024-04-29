"""
Program: copyfile.py
Author: Cesar Guevara

8. Write a script named copyfile.py. This script should prompt the user for the
names of two text files. The contents of the first file should be input and written
to the second file. filename: copyfile.py


1. Significant constants:

	None

2. The inputs are:
	
	firstFile
	secondFile

3. Computations:

	none

4. The outputs are:

	the script returns no values
"""

# Initialize the constants

# Request inputs

firstFile=input("Insert the name of the first file:")
secondFile=input("Insert the name of the second file:")
# Computations
firstFile=open(firstFile,'r')
secondFile=open(secondFile,'w')
secondFile.write(firstFile.read())
# Display results
