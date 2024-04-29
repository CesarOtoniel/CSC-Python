"""
Program: concordance.py
Author: Cesar Guevara

A file concordance tracks the unique words in a file and their frequencies.
 Write a program in the file concordance.py that displays a concordance for 
a file. The program should output the unique words and their frequencies 
in alphabetical order. Variations are to track sequences of two words and 
their frequencies, or n words and their frequencies.

1. Significant constants:

2. The inputs are:
	fileName #Name of the file to analyze
3. Computations:
	wordFreq #dictionary with the words and their frequencies
4. The outputs are:
	wordFreq #output the dictionary once sorted
"""

# Define functions
def cleanText(text):
	word='' #buffer for words
	words = []

	for char in text:
		if char.isalpha():
			word += char
		else:
			if word:	#Flushes buffer
				words.append(word.lower())
				word = ''
	if word:
		words.append(word.lower())
	
	return words

def countWords(wlist):
	wordFreq = {} #empty dictionary
	for word in wlist:
		if word in wordFreq:
			wordFreq[word] += 1
		else:
			wordFreq[word] = 1
	return wordFreq

# Request inputs
fileName = input("Enter a file to analyze: ")

file = open(fileName,"r")

text=cleanText(file.read())

# Computations
concordanceDict=countWords(text)
# Display results

print(sorted(concordanceDict))
