for i in range(0,100):
	if i % 3 == 0 and i % 5 == 0:
		print(str(i) + ': fizz-buzz')
	elif i % 3 == 0:
		print(str(i) + ": Fizz")
	elif i % 5 == 0:
		print(str(i) + ": Buzz")
	else:
		print(i)