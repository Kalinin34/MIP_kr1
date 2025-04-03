from AI.AITreeItem import AITreeItem
from Tree import Tree

#Koks modificçts lai darbotos ar MI 
class AITree(Tree):
    def __init__(self, FirstVariable):
        self.Item = AITreeItem(FirstVariable,0)
        self.Item.minmax = 'x'
        self.len = 1

    
    def Add(self,variable : int,address : list):
        self.__Add__(self.Item,variable,address)
        pass

    def __Add__(self,item: AITreeItem , variable : int, address : list):
        if(address.__len__() == 1):
            match address[0]:
                case 'L':
                    item.setL(variable,self.len,item.minmax)
                    pass
                case 'R':
                    item.setR(variable,self.len,item.minmax)
                    pass
            self.len += 1
        else:
            nextAddres = address.pop(0)
            match nextAddres:
                case 'L':
                    if(item.L != None):
                        self.__Add__(item.L,variable,address)
                    else:
                        raise ValueError("Nepareizi ievadita addrese")
                    pass
                case 'R':
                    if(item.R != None):
                        self.__Add__(item.R,variable,address)
                    else:
                        raise ValueError("Nepareizi ievadita addrese")
                    pass
        pass
