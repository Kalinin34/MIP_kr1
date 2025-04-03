import array
from AI.AI import AI
from UserGraphicInterface import GameSetupWindow as Interface

class GameManager:
    def __init__(self):
        self.reset()
    
    def reset(self):
        #skaitlis kas sakuma izvelas speletajs un kuru dala uz 3 vai 2
        self.currentVal = 0 
        #speletaja punktu skaits
        self.player = 0 
        #datora punktu skaits
        self.computer = 0 
        #banka punktu skaits
        self.Bank = 0
        #gajienu koks
        self.Tree = None
        #mainîgais kurð saglaba adresi uz pedejo koka virsotni
        self.currentWay = []
        #mainîgas kurð atbildîgs par speles statusu
        self.game_over = False
        #MI ar minmax un alfabeta algoritmu
        self.AI = None

    #Pârada iespçjamas ceïas ar tagadejo skaitli
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

    #Pievieno MI ar izveleto algoritmu
    def setAI(self,algoritms):
        self.AI = AI(algoritms)
    
    #Inicianalize interfeisu
    def initGUI(self):
        self.Uinterface = Interface(self)
        pass
    #Iesledz GUI
    def run(self):
        self.Uinterface.mainloop()

