"""
Program: unique.py
Author: Cesar Guevara
Write a program in the file unique.py that inputs a text file. 
The program should print the unique words in the file in alphabetical order. 


1. Significant constants:
	none
2. The inputs are:
	fileName
3. Computations:
	words
4. The outputs are:
	sortedWords
"""
def cleanText(text):
	word='' #buffer for words
	words = []

	for char in text:
		if char.isalpha():
			word += char
		else:
			if word:        #Flushes buffer
				words.append(word.lower())
				word = ''
	if word:
		words.append(word.lower())

	return words

def uniqueList(wlist):
	uniqueWords = [] #empty list
	for word in wlist:
		if word in uniqueWords:
			pass
		else:
			uniqueWords.append(word)
	return uniqueWords

def main():
# Initialize the constants
#Ask for user input
	fileName= input("Input a file name: ")
	file = open(fileName,'r')
	text = file.read()
#Computations
	sortedWords= sorted(uniqueList(cleanText(text)))

#Display results
	print(sortedWords)

if __name__ == '__main__':
	main()
