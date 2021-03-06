import time

def calculate_time(func):
	"""
	Decorator that displays the amount of time a given function takes

	Parameters
	----------
	func: function
		The function that will be timed 

	Returns
	-------
		Returns "Total time X" where X is the amount of timt the funciton took

	
	
	"""

	def rapper():

		t1 = time.time()
		func()
		t2 = time.time()
		totTime = t2 - t1

		print ("Total time ", totTime)
	return rapper


@calculate_time
def say_whee():
	"""
	Funciton used to test the calculate_time decorator
		Simply print "WHee" then gets timed using the calculate_time funciton

	Function taken from examples in lecture
		
	"""
	print("WHee")

say_whee()

