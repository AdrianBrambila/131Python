def calculator(number1, number2, operator):
	"""
	Calculator function, adds, subtracts, multiplies, divides, integer divides, and does power finctions

	Parameters
	-----------
	number1: float
		first number to be calculated
	number2: float
		Second number to be calculated
	operator: string
		Operation to be performed

	Returns
	-------
	float
		The final number after the given operation is performed



	"""

	number1 = float(number1)
	number2 = float(number2)

	if operator == '+':
		total = number1 + number2
		total = float(total)
		return total


	elif operator  == '-':
		total = number1 - number2
		total = float(total)
		return total

		
	elif operator == '*':
		total = number1 * number2
		total = float(total)
		return total

	elif operator == '/':
		
		total = number1 / number2
		total = float(total)
		return total

	elif operator == '//':
		total = number1 // number2
		total = float(total)
		return total

	elif operator == '**':
		total = pow(number1, number2)
		total = float(total)
		return total

	else:
		print("Invalid Input!!")

def main():
	"""
	Main function takes user inputs for the parameters, amd allows user to exit if they wish to no longer use the calculator

	Parameters
	----------
	None


	Returns
	-------
	string
		returns the total for the operation the user inputs after the calculator function runs

	"""

	number1 = int(input("Enter the first number: "))
	

	number2 = int(input("Enter the second number: "))
	

	operation = input("Enter the operation: ")
	
	
	print(calculator(number1, number2, operation), "\n")
	
		
	exit = 'n'
	while exit != 'y':
	
		exit = input("Do you wish to exit? ")

		if exit == 'y':
			print(">>>")
			break


		number1 = input("Enter the first number: ")
	

		number2 = input("Enter the second number: ")
		

		operation = input("Enter the operation: ")
		
		
		print(calculator(number1, number2, operation), "\n")




main()



 
