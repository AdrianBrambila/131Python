def calculate_apr(principal, interest_rate, years):
	"""
	This function calculates the amount of interest earned on an initial investment. 
	
	Parameters
	-----------
	principal: float
		Initial investment
	interest_rate: float
		The interest rate
	years: float
		Amount of time of investment

	
	Returns
	----------
	float
		The total amount in the investment acount with the given rate after the given time
	
	Tested with $500 initial, 3% rate and 65 years

	"""
	
	
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



		
