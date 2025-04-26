operator = input("enter operator:")
first_number = input("enter first number:")
second_number = input("enter second number:")
output=""
if (operator=="+"):
    output=int(first_number) + int(second_number)
    print(output)
elif(operator=="-"):
    output=int(first_number) - int(second_number)
    print(output)
elif(operator=="*"):
    output=int(first_number) * int(second_number)
    print(output)
elif(operator=="/"):
    output=int(first_number) / int(second_number)
    print(output)