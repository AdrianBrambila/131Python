def calculate_apr(principal, interest_rate, years):
	
	
	if principal < 0:
		
		return false
	elif interest_rate < 0:
		
		return false
	elif years < 0:
		
		return false
	else:
		num1 = (1 + interest_rate)**years
		print("num1: ", num1)

		final = num1 * principal
		finalFloat = float(final)

		print(finalFloat)

		return finalFloat

calculate_apr(500, .03, 65)



		
