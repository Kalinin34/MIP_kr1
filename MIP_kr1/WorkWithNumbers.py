import random as Random

def RandomVariablesForGame(min,max,length):
    randArray = []
    while(randArray.__len__() <5):
        v = Random.randrange(min,max)
        if(v%2==0) and (v%3==0):
            randArray.append(v)
    return randArray
