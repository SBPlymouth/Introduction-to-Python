# -*- coding: utf-8 -*-

import random
import string
class passgen:
	#initialize lists using string library
	def __init__(self, password = "", alphabet=list(string.ascii_letters), alphnum=(list(string.ascii_letters)+list(string.digits)), printable=(list(string.ascii_letters)+list(string.digits) + ['!', '@', '#', '$', '%', '^', '&', '*', "(", ')']) ): 
		self.alphabet = alphabet 
		self.alphnum = alphnum
		self.printable = printable
		self.password = password
	def weak(self, length):
		password = ""
		for i in range(length):
			password += random.choice(self.alphabet)
		self.password = password
		return password
	def fair(self, length):
		password = ""
		for i in range(length):
			password += random.choice(self.alphnum)
		self.password = password
		return password
	def strong(self, length):
		password = ""
		for i in range(length):
			password += random.choice(self.printable)
		self.password = password
		return password
	def choose(self):
		length = int(input('Enter Desired Password Length: ')) #allows user to pick password length
		strength = int(input('Select Desired Password Strength:\n 1: Weak\n 2: Fair\n 3:Strong\n Selection: ')) #allows user to pick password strength
		if strength == 1: #checks what the user picked for strength then calls appropriate method
			self.weak(length)
		elif strength == 2:
			self.fair(length)
		elif strength == 3:
			self.strong(length)
		else: # if they entered something invalid tell them they can't
			print('invalid selection')
			self.choose() # run the function again. this is optional and can be replaced with an end of program

a = passgen()
a.choose()
print(a.password)
		