x = True
while x: 
    p= input("Input your password:") 
    if (len(p)<6 or len(p)>12):
        print("Invalid Password")
        x=True
    else:
        print("Valid Password")
        x=False
        break
