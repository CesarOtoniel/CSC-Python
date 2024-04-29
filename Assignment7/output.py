   2>"""
   3>Program: lightyear.py
   4>Author: Cesar Guevara
   5>
   6>
   7>9. Write a script named numberlines.py. This script creates a program listing from a
   8>source program. This script should prompt the user for the names of two files. The
   9>input filename could be the name of the script itself, but be careful to use a different
  10>output filename! The script copies the lines of text from the input file to the output
  11>file, numbering each line as it goes. The line numbers should be right-justified in
  12>4 columns, so that the format of a line in the output file looks like this example:
  13>1> This is the first line of text. 
  14>
  15>
  16>1. Significant constants:
  17>
  18>	None
  19>
  20>2. The inputs are:
  21>	
  22>	firstFile
  23>	secondFile
  24>
  25>3. Computations:
  26>
  27>	lineNumber
  28>
  29>4. The outputs are:
  30>
  31>	the script returns no values
  32>"""
  33>
  34># Initialize the constants
  35>
  36># Request inputs
  37>
  38>firstFile=input("Insert the name of the first file:")
  39>secondFile=input("Insert the name of the second file:")
  40># Computations
  41>firstFile=open(firstFile,'r')
  42>secondFile=open(secondFile,'w')
  43>lineNumber = 1
  44>for line in firstFile:
  45>	lineNumber+=1
  46>	secondFile.write("%4s%1s%s" % (lineNumber,'>', line))
  47># Display results
