"""
Program: dif.py
Author: Cesar Guevara

10. Write a script named dif.py. This script should prompt the user for the names
of two text files and compare the contents of the two files to see if they are the
same. If they are, the script should simply output "Yes". If they are not, the script
should output "No", followed by the first lines of each file that differ from each
other. The input loop should read and compare lines from each file. The loop
should break as soon as a pair of different lines are found.

1. Significant constants:

	None

2. The inputs are:
	
	firstFile
	secondFile

3. Computations:

	lineNumber

4. The outputs are:

	the script returns no values
"""

# Initialize the constants

# Request inputs

firstFile=input("Insert the name of the first file:")
secondFile=input("Insert the name of the second file:")
# Computations
firstFile=open(firstFile,'r')
secondFile=open(secondFile,'r')
counter = 0
while True:
	counter=counter+1
	line1 = firstFile.readline()
	line2 = secondFile.readline()
	if line1==line2:
		pass
# Display results
	else:
		print(f'No {line1} {line2}')
		break
	if line1==line2 and line1=='':
		print('Yes')
		break
