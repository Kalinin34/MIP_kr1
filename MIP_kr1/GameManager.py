import array
from AI.AI import AI
from UserGraphicInterface import GameSetupWindow as Interface

class GameManager:
    def __init__(self):
        self.reset()

    def reset(self):
        self.currentVal = 0 
        self.player = 0 
        self.computer = 0 
        self.Bank = 0
        self.Tree = None
        self.currentWay = []
        self.game_over = False
        self.AI = None
    def robBank(self,player):
        player += self.Bank
        pass

    def observe(self):
        item = self.Tree.Item
        localWay = list(self.currentWay)
        while localWay.__len__()!= 0:
            goTo = localWay.pop(0)
            match goTo:
                case 'L':
                    item = item.L
                    continue
                case 'R':
                    item = item.R
                    continue
        if(self.currentVal%2==0):
            lway = list(self.currentWay)
            lway.append('L')
            self.Tree.Add(self.currentVal/2,lway)
            

        if(self.currentVal%3==0):
            rway = list(self.currentWay)
            rway.append('R')
            self.Tree.Add(self.currentVal/3,rway)

        pass
    
    def chooseVal(self,arr,index):
        self.Num = arr[index]
        pass

    def setAI(self,algoritms):
        self.AI = AI(algoritms)

    def initGUI(self):
        self.Uinterface = Interface(self)
        pass
    def run(self):
        self.Uinterface.mainloop()

