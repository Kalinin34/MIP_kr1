import math
import random
from AI.AITree import AITree, AITreeItem

#MI klase
class AI:
    #Inicializēšana
    def __init__(self,method):
        self.AiTree = None
        self.method = method
        pass

    #metodes izvēlešana
    def thinking(self,number,AiScoreCount,playerScoreCount,bank):
        self.AiTree = AITree(number)
        #Ģenere koku ar viesiem iespējamiem skaitliem
        self.__generateTree__(number)
        print(f"value = {number}")

        print(f"AiScoreCount = {AiScoreCount}, playerScoreCount= {playerScoreCount}")
        
        #Inicialize pedejos skaitļus (uzvari,neitrali,sakavi)
        self.__setEnding__(self.AiTree.Item,0,True,playerScoreCount,AiScoreCount,bank)
        #Nakotnē izvelets skaitlis
        dirSum = 0
        #Pēc izvēleta methodes algoritma izpildīšana
        match(self.method):
            case 'minimax':
                dirSum = self.__minmaxMethod__(self.AiTree.Item)
                pass
            case 'alpha_beta':
                alpha = float('-inf')
                beta = float('inf')
                dirSum = self.__alfabeta__(self.AiTree.Item,alpha,beta)
                pass
        
        #ceļu izvēlēšana
        if(self.AiTree.Item.L is not None and self.AiTree.Item.R is None):
            self.direction = True

        if(self.AiTree.Item.R is not None and self.AiTree.Item.L is None):
            self.direction = False

        if(self.AiTree.Item.R is not None and self.AiTree.Item.L is not None):
            if(self.AiTree.Item.L.AIvalue == self.AiTree.Item.R.AIvalue):
                self.direction = random.choice([True,False])
            elif(self.AiTree.Item.L.AIvalue ==dirSum):
                self.direction = True
            else:
                self.direction = False

        # if(number < 700):
        #     import AI.AiVisualisation
        #     AI.AiVisualisation.Output_treeAI(self.AiTree)
        # true = kreisi / false = labi

        pass

    #pavisam ģenere koku
    def __generateTree__(self,number):
        wlist = []
        self.__generateTreeItemAdd__([],number,wlist)
        for i in range(len(wlist)):
            variable,address = wlist[i]
            self.AiTree.Add(variable,address)
        pass
    
    #koka virsotņu generacijas metode
    def __generateTreeItemAdd__(self,path: list, numb, wlist: list):
        if(numb==1):
            pass
        #ja skaitlis dalas ar 2 tad ģenero kreiso zaru
        if(numb%2==0 and int(numb/2)!=1):
            localpath = path.copy()
            localNum = numb/2
            localpath.append('L')
            wlist.append([localNum,localpath])
            self.__generateTreeItemAdd__(localpath,localNum,wlist)
        #ja skaitlis dalas ar 3 tad ģenero labo zaru
        if(numb%3==0 and int(numb/3)!=1):
            localpath = path.copy()
            localNum = numb/3
            localpath.append('R')
            wlist.append([localNum,localpath])
            self.__generateTreeItemAdd__(localpath,localNum,wlist)
        pass
    
    #iespejāmo soļu konstruēšana un min/max pievienošana
    def __setEnding__(self,item: AITreeItem, depth, solis, player, computer, bank):
        if(item.L == None and item.R == None):
            if(solis):
                print("a")

                if(item.value%2==0):
                    player += 1
                else:
                    player -=1

                if (item.value%5==0):
                    bank += 1
                item.minmax = 'x'
            else:
                if(item.value%2==0):
                    computer += 1
                else:
                    computer -=1


                if (item.value%5==0):
                    bank += 1
                item.minmax = 'n'
            if(item.value == 2):
                if(solis):
                    computer += bank
                else:
                    player += bank
            if(computer>player):
                item.AIvalue = 1
            elif(computer==player):
                item.AIvalue = 0
            else:
                item.AIvalue = -1
            
            print(f"Aivalue = {item.AIvalue},value = {item.value}, depth={depth}  minmax = {item.minmax} а")
            print(f"player = {player} comp = {computer}bank = {bank} minmax = {item.minmax}")
            return
        if(depth>0):
            if(solis):
                if(item.value%2==0):
                    computer += 1
                else:
                    computer -=1

                if (item.value%5==0):
                    bank += 1
                item.minmax = 'x'
                item.AIvalue = float("-inf")
            else:
                if(item.value%2==0):
                    player += 1
                else:
                    player -=1

                if (item.value%5==0):
                    bank += 1
                item.minmax = 'n'
                item.AIvalue = float("inf")
            #print(f"itemvalue = {item.value} player = {player} comp = {computer} bank = {bank} minmax = {item.minmax} solis = {solis}")
            if(item.L != None):
                self.__setEnding__(item.L,depth+1,not solis,player,computer,bank)
            if(item.R != None):
                self.__setEnding__(item.R,depth+1,not solis,player,computer,bank)    
        else:
            if(item.L != None):
                self.__setEnding__(item.L,depth+1,not solis,player,computer,bank)
            if(item.R != None):
                self.__setEnding__(item.R,depth+1,not solis,player,computer,bank)
            item.AIvalue = float("-inf")
            item.minmax = 'x'
        pass

    #minmax metode
    def __minmaxMethod__(self,item: AITreeItem):
        if(item.L == None and item.R == None):
            return item.AIvalue
        LVal = 0
        RVal = 0

        if item.L != None:
            LVal =  self.__minmaxMethod__(item.L)
        else:
            LVal = None

        if item.R != None:
            RVal =  self.__minmaxMethod__(item.R)
        else:
            RVal = None

        if LVal == None:
            item.AIvalue = RVal
            return RVal

        if RVal == None:
            item.AIvalue = LVal
            return LVal

        match(item.minmax):
            case 'n':
                tmp = min(LVal,RVal)
                if(LVal == RVal):
                    item.AIvalue = LVal
                elif(tmp == LVal):
                    item.AIvalue = LVal
                else:
                    item.AIvalue = RVal
                return tmp
            case 'x':
                tmp = max(LVal,RVal)
                if(LVal == RVal):
                    item.AIvalue = LVal
                elif(tmp == LVal):
                    item.AIvalue = LVal
                else:
                    item.AIvalue = RVal
                return tmp
        pass

    #alfabeta metode
    #Generated ar ChatGPT
    def __alfabeta__(self,item: AITreeItem,alpha, beta):
        if(item.L == None and item.R == None):
            return item.AIvalue

        if item.minmax == 'x':  
            max_eval = float('-inf')
            if item.L is not None:
                eval_L = self.__alfabeta__(item.L, alpha, beta)
                max_eval = max(max_eval, eval_L)
                alpha = max(alpha, eval_L)
                if beta <= alpha:
                    return max_eval  

            if item.R is not None:
                eval_R = self.__alfabeta__(item.R, alpha, beta)
                max_eval = max(max_eval, eval_R)
                alpha = max(alpha, eval_R)
                if beta <= alpha:
                    return max_eval  
            item.AIvalue = max_eval
            return max_eval
        else:
            min_eval = float('inf')

            if item.L is not None:
                eval_L = self.__alfabeta__(item.L, alpha, beta)
                min_eval = min(min_eval, eval_L)
                beta = min(beta, eval_L)
                if beta <= alpha:
                    return min_eval 

            if item.R is not None:
                eval_R = self.__alfabeta__(item.R, alpha, beta)
                min_eval = min(min_eval, eval_R)
                beta = min(beta, eval_R)
                if beta <= alpha:
                    return min_eval 

            item.AIvalue = min_eval
            return min_eval

