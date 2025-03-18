class TreeItem:
    def __init__(self,value,index):
        self.value = value
        self.L = None
        self.R = None
        self.index = index
        pass

    def setL(self,variable,index):
        self.L = TreeItem(variable,index)
        pass

    def setR(self,variable,index):
        self.R = TreeItem(variable,index)
        pass
