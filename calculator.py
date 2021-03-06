def calculator(number1, number2, operator):
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



 
