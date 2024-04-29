"""
Program: testSorted.py
Author: Cesar Guevara


A list is sorted in ascending order if it is empty or
each item except the last one is less than or equal to
its successor. Define a predicate isSorted that expects
a list as an argument and returns True if the list is
sorted or returns False otherwise. (Hint: For a list of
length 2 or greater, loop through the list and compare
pairs of items, from left to right, and return False if
the first item in a pair is greater.) Include the function
in a short tester program in the file named testsort.py.

1. Significant constants:

2. The inputs are:

3. Computations:

4. The outputs are:

"""

# Initialize the constants

# Request inputs

# Computations

# Display results

def isSorted(myList):
	if myList == {}:
		return True
	else:
		for element in range(len(myList)-1):
			if myList[element+1]<myList[element]:
				return False
			else:
				pass
		return True


def main():
	myLists = [
		[1,2,3,4,5,6,7,8,9],
		[],
		[3,1,2,4],
		['a'+'b'+'c'+'d'],
		['A','a','B']
		]
	for data in myLists:
		if isSorted(data):
			print(f"The list {data} is sorted")
		else:
			print(f"The list {data} is not sorted")
if __name__ == '__main__':
	main()
