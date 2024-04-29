"""
Program: commandinterpreter.py
Author: Cesar Guevara
Design, implement, and test a program in the file named 
commandinterpreter.py that uses a simple text-based command 
interpreter. Here is a sample session with the program: 
	1 Open
	2 Save
	3 Compile
	4 Run
	5 Quit
	Enter a number: 2
	Command = Save

The program should define three other functions, named 
printMenu , acceptCommand , and performCommand , to carry
out steps a, b, and c, respectively. The function to display
the menu expects a list of menu options as an argument and 
displays these options prefixed with numbers. The function 
to accept an input command expects the length of the menu 
list as an argument. The function repeatedly prompts the user 
for a number in the range of options and takes inputs until the 
user enters a number within the range. The function either 
displays an error message for an invalid input or returns a 
valid input. The function to perform a command takes a command 
number and the menu as arguments and displays the selected 
command in the menu. Test your program with the menu 
["Open", "Save", "Compile", "Run", "Quit"] and at least one 
other menu. Note that all menus must include a "Quit" command 
as the last item in the menu. (LO: 6.2)

1. Significant constants:
	functions
2. The inputs are:
	command
3. Computations:
	no computations made
4. The outputs are:
	none
"""
# Function definitions
def Open():
	pass
def Save():
	pass
def Compile():
	pass
def Run():
	pass
def Quit():
	print("Have a nice day!")

def printMenu(functions):
	for i in functions:
                print(i," ",functions[i].__name__)

def acceptCommand(command,functions):
	if command in functions:
		print(f"Command = {currentMenu[command].__name__}")
		return True
	else:
		print("Please insert a valid command: ")
		return False
def performCommand(command,function):
	function = currentMenu[command]()
# Initialize the constants

functions = {	'1':Open,
		'2':Save,
		'3':Compile,
		'4':Run,
		'5':Quit}

#This is an alternative menu, same functions in different order
functions2 = {  'sa':Save,
                'op':Open,
                'ru':Run,
                'co':Compile,
                'qu':Quit}

currentMenu=functions #This flag selects the menu change it to switch menus
def main():
	# Ask for inputs
	while True:
		printMenu(currentMenu)
		command = input("Enter a function: ")
		if acceptCommand(command,currentMenu):
	# Display Results
			performCommand(command,currentMenu)
			if currentMenu[command].__name__ == 'Quit':
	#Breaks loop when function Quit is called
				break
		else:
			print("Please enter a valid input")
if __name__ == '__main__':
	main()
