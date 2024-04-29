"""
Program: stats.py
Author: Cesar Guevara

A group of statisticians at a local college has asked 
you to create a set of functions that compute the median
 and mode of a set of numbers, as defined in Section 5.4.
 Define these functions in a module named stats.py. 
Also include a function named mean , which computes the
average of a set of numbers. Each function should expect 
a list of numbers as an argument and return a single number.
 Each function should return 0 if the list is empty. 
Include a main function that tests the three statistical 
functions with a given list.

1. Significant constants


2. The inputs are:
	data

3. Computations:
	statisticalMode
	statisticalMean
	statisticalMedian

4. The outputs are:
	statisticalMode
        statisticalMean
        statisticalMedian

4. The functions created for this file are:
	sMode(data)	;returns the statistical mode of a list of values
	sMedian(data)	;returns the statistical median of a list of values
	sMean(data)	;returns the statistical mean of a list of values

"""
# Functions

def sMean(data):
	if len(data) == 0:
		return 0
	else:
		statisticalMean=0.0
		for item in data:
			statisticalMean=statisticalMean+float(item)
		statisticalMean=statisticalMean/len(data) 
		return statisticalMean

def sMode(data):
	if len(data) == 0:
		return 0
	else:
		datapoints=[]
		for item in data:
			if item in datapoints:
				pass
			else:
				datapoints.append([item,data.count(item)])
		statisticalMode=0
		lastval=0
		for i in range(len(datapoints)):
			if datapoints[i][1]>lastval:
				lastval=datapoints[i][1]
				statisticalMode=datapoints[i][0]
		return statisticalMode

def sMedian(data):
	median = 0
	if len (data) == 0:
		return median
	else:
		data.sort()
		if len(data) % 2 == 1:
			median=data[len(data)//2]
		else:
			median=(float(data[len(data)//2])+float(data[len(data)//2-1]))/2
	return median

def main():
# Initialize the constants

# Request inputs
	data=input("Please insert the data separated by commas: ")
	if len(data) == 0:
		return 0
	data=data.split(',')
# Computations
	statisticalMean=sMean(data)
	statisticalMode=sMode(data)
	statisticalMedian=sMedian(data)
	print(f"The mean of the dataset is : {statisticalMean}")
	print(f"The mode of the datashet is: {statisticalMode}")
	print(f"The median of the dataset is: {statisticalMedian}")
# Display results
if __name__ == "__main__":
	main()
