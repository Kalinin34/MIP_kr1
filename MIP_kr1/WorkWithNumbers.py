import random as Random

#Nejauðo skaitïu ìenerçðana
def RandomVariablesForGame(minM,maxM,length):
    randArray = []
    while(randArray.__len__() <5):
        Fnumber = 1
        while True:
            Fnumber *= Random.randint(2,3)
            if(minM<Fnumber):
                break
        access = True
        for x in randArray:
            if x == Fnumber:
                access = False;
                pass
            pass
        if(maxM>Fnumber and access):
            randArray.append(Fnumber)
    return randArray
