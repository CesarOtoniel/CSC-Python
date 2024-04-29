"""
Program: employeepay.py
Author: Cesar Guevara

1. Significant constants:
	overtimeRate=1.5
2. The inputs are:
	totalHours
	wage
3. Computations:
	overtimePay=overtimeRate*overtimeHours
	overtimeHours=regularHours-40
	regularHours=totalHours-overtimeHours
4. The outputs are:
	totalPay
"""

# Initialize the constants
overtimeRate=1.5
# Request inputs
#totalHours=float(input("Insert number of worked hours: "))
wage=float(input("Please insert the hourly rate: "))
regularHours=float(input("Please insert the number of regular hours: "))
overtimeHours=float(input("Insert number of overtime hours:  "))

# Computations
"""if (totalHours<=40):
	regularHours=totalHours
	overtimeHours=0
else:
	overtimeHours=totalHours-40.0
	regularHours=40
"""

totalPay=(regularHours+overtimeHours*overtimeRate)*wage
print(f"This employee made ${totalPay} on this pay period")
# Display results
