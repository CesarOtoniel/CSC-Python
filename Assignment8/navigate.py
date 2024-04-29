"""
Program: navigate.py
Author: Cesar Guevara
Write a program in the file navigate.py that allows the user to navigate
the lines of text in a file. The program should prompt the user for a 
filename and input the lines of text into a list. The program then 
enters a loop in which it prints the number of lines in the file and
 prompts the user for a line number. Actual line numbers range from 1 
to the number of lines in the file. If the input is 0, the program quits. 
Otherwise, the program prints the line associated with that number. 

1. Significant constants:
	ESCAPE_CHAR # escape character
2. The inputs are:
	filemame #name of the file to navigate
	lineN	#number of line to navigate to
3. Computations:
	docList
	nLinesDoc
4. The outputs are:
	result #text of the line chosen by the user
"""

# Initialize the constants
ESCAPE_CHAR='0' #a input of 0 will terminate the program
nLinesDoc=0
# Request inputs

filename=input("Enter the name of the file to read: ")
docList = []
# Computations
with open(filename,'r') as file:
	for line in file:
		print(line.strip())
		docList.append(line.strip())
		nLinesDoc=nLinesDoc+1
#Request input

while(1):
	reqLine = input(f"File {filename} loaded, enter a line number between 1 and {nLinesDoc} :")
	if reqLine == ESCAPE_CHAR:
		break
#Display Results
	else:
		print(docList[int(reqLine)-1])
