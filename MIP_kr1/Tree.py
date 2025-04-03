from TreeItem import TreeItem

#Koks
class Tree:
    def __init__(self,FirstVariable):
        self.Item = TreeItem(FirstVariable,0)
        self.len = 1
        pass

    #pievienoðana kokam elementu
    def Add(self,variable : int,address : list):
        self.__Add__(self.Item,variable,address)
        pass
    #pievienoðana kokam elementu(iekðeja funkcija)
    def __Add__(self,item: TreeItem , variable : int, address : list):
        if(address.__len__() == 1):
            match address[0]:
                case 'L':
                    item.setL(variable,self.len)
                    pass
                case 'R':
                    item.setR(variable,self.len)
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
