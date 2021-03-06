import time

def calculate_time(func):
	def rapper():

		t1 = time.time()
		func()
		t2 = time.time()
		totTime = t2 - t1

		print ("Total time", totTime)
	return rapper


@calculate_time
def say_whee():
	print("WHee")

say_whee()

