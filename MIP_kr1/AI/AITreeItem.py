import sys

from TreeItem import TreeItem

class AITreeItem(TreeItem):
    def __init__(self, value, index):
        super().__init__(value, index)
        #identifikators kurð kura stavokïa atrodas virsotne
        self.minmax = None
        #skaitïa uzvares vai sakaves identifikators(vai -1...1) minimax algoritmam
        self.AIvalue = 0

    def setL(self,variable,index,minmax):
        self.L = AITreeItem(variable,index)
        pass

    def setR(self,variable,index,minmax):
        self.R = AITreeItem(variable,index)
        pass

    def setMinMax(self,minmax):
        self.minmax = minmax
        pass
    def setAIValue(self,AIvalue):
        self.AIvalue = AIvalue
        pass
