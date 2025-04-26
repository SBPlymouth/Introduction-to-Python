import random

def randgen(max):
    return random.randint(1,max)
    
def coinflip():
    coin = random.randint(1,2)
    if coin == 1:
        return "Heads"
    else:
        return "Tails"
def average(Heads, Tails):
    print("Heads: " + str(Heads))
    print("Tails: " + str(Tails))
    total = Heads + Tails
    print("Total: " + str(total))
    print("Heads: " + str((Heads/total)*100) + "%")
    print("Tails: " + str((Tails/total)*100) + "%")
    
def simulation():
    Heads = 0
    Tails = 0
    for i in range(randgen(100)):
        flip = coinflip()
        if flip == "Heads":
            Heads += 1
        else:
            Tails += 1
    average(Heads, Tails)
    
simulation()