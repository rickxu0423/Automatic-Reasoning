class Tree:
    def __init__(self, tree=None, symbol=None, parent=None, left=None, right=None):
        if tree != None:
            self.symbol = tree.symbol
            self.left = tree.left
            self.right = tree.right
            self.parent = tree.parent
        else: 
            self.symbol = symbol
            self.left = left
            self.right = right
            self.parent = parent
    
    def __str__(self):
        return self.symbol

    def getSymbol(self):
        return self.symbol

    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def getParent(self):
        return self.parent