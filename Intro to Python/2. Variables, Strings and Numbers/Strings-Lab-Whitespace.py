# Copyright STEM Builders inc - All rights reserved

print("Hello everyone!") 
# Output: 
# Hello everyone!

print("\tHello everyone!") 
# Output: 
# 	Hello everyone!

print("Hello \teveryone!") 
# Output: 
# Hello 	everyone!

# The combination "\n" makes a newline appear in a string. You can use newlines anywhere you like in a string.
print("Hello everyone!") 
# Output: 
# Hello everyone!

print("\nHello everyone!") 
# Output: 
# Hello everyone!

print("Hello \neveryone!") 
# Output: 
# Hello  everyone!

print("\n\n\nHello everyone!") 
# Output: 
#   Hello everyone!


name = ' eric '  
print(name.lstrip()) 
print(name.rstrip()) 
print(name.strip()) 
# Output: 
# eric   eric eric

# It's hard to see exactly what is happening, so maybe the following will make it a little more clear:
name = ' eric '  
print('-' + name.lstrip() + '-') 
print('-' + name.rstrip() + '-') 
print('-' + name.strip() + '-') 
# Output: 
# -eric - - eric- -eric-
