import copy
class Formula:

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


class Atom(Formula):

    def calculate(self, data):
        return data[self.symbol]
    def generateClauses(self, temSet):
        symbol = self.symbol.split(',')
        return frozenset(symbol)


class Negation(Formula):
    def __init__(self, tree=None, symbol=None, parent=None, left=None, right=None):
        super().__init__(tree, symbol, parent, left, right)
        self.symbol = "~"
    def calculate(self, data):
        return not self.left.calculate(data)
    def generateClauses(self, temSet):
        temSymbol = "~"+ self.left.symbol
        symbol = temSymbol.split(',')
        return frozenset(symbol)

class Conjunction(Formula):
    def __init__(self, tree=None, symbol=None, parent=None, left=None, right=None):
        super().__init__(tree, symbol, parent, left, right)
        self.symbol = "^"
    def calculate(self, data):
        if not self.left.calculate(data) or not self.right.calculate(data):
            return False
        else:
            return True
    def generateClauses(self, temSet):
        left = self.left.generateClauses(temSet)
        right = self.right.generateClauses(temSet)
        if type(left) == frozenset:
            temSet.add(left)
        else:
            temSet = temSet.union(left)
        if type(right) == frozenset:
            temSet.add(right)
        else:
            temSet = temSet.union(right)
        return temSet

class Disjunction(Formula):
    def __init__(self, tree=None, symbol=None, parent=None, left=None, right=None):
        super().__init__(tree, symbol, parent, left, right)
        self.symbol = "v"
    def calculate(self, data):
        if not self.left.calculate(data) and not self.right.calculate(data):
            return False
        else:
            return True
    def generateClauses(self,temSet): 
        left = self.left.generateClauses(temSet)
        right = self.right.generateClauses(temSet)
        result = frozenset(set(left).union(set(right)))
        return result

class Implication(Formula):
    def __init__(self, tree=None, symbol=None, parent=None, left=None, right=None):
        super().__init__(tree, symbol, parent, left, right)
        self.symbol = "=>"
    def calculate(self, data):
        if self.left.calculate(data) and not self.right.calculate(data):
            return False
        else:
            return True

class Biconditional(Formula):
    def __init__(self, tree=None, symbol=None, parent=None, left=None, right=None):
        super().__init__(tree, symbol, parent, left, right)
        self.symbol = "<=>"
    def calculate(self, data):
        if self.left.calculate(data) and self.right.calculate(data):
            return True
        elif not self.left.calculate(data) and not self.right.calculate(data):
            return True
        else:
            return False
