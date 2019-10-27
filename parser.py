from formula import Formula, Atom, Negation, Conjunction, Disjunction, Implication, Biconditional
import copy

operatorList = ['^', 'v', '~', '=>', '<=>']
afterList = ['(', '>']
beforeList = [')', '=', '<']

def splitString(logic):
    RList = []
    for i in range(len(logic)):
        j = 0
        while j < len(logic[i]):
            if logic[i][j] in afterList and logic[i][j+1] != " ":
                logic[i] = logic[i][:j+1] + " " + logic[i][j+1:] 
                j += 2
            elif logic[i][j] in beforeList and logic[i][j-1] != '<' and logic[i][j-1] != " ":
                logic[i] = logic[i][:j] + " " + logic[i][j:] 
                j += 1
            elif logic[i][j] in operatorList:
                if logic[i][j-1] != " ":
                    logic[i] = logic[i][:j] + " " + logic[i][j:]
                    j += 1
                if  logic[i][j+1] != " ":
                    logic[i] = logic[i][:j+1] + " " + logic[i][j+1:] 
                    j += 2        
            else:
                j += 1
        token = logic[i].strip().split(' ')
        RList.append(token)
    return RList

def getSymbols(RList, alphaList):
    symbolSet = set()
    for R in RList:
        temList = [x for x in R if x not in operatorList + afterList + beforeList]
        temSet = set(temList)
        symbolSet = symbolSet.union(temSet)
    for R in alphaList:
        temList = [x for x in R if x not in operatorList + afterList + beforeList]
        temSet = set(temList)
        symbolSet = symbolSet.union(temSet)
    return symbolSet


def parseToTree(symbol, node):

    if symbol not in operatorList or symbol == "~":
        if symbol == ")":
            while 1:
                node = node.parent
                if node.symbol != "~":
                    break
            if node.symbol == None:
                if node.parent != None and node.parent.symbol != "~":
                    node.parent.right = node.left
                else:
                    node.parent.left = node.left
                
                return node
            else:
                return node
        elif node.symbol == None or node.symbol == "~":
            if symbol == "(":
                node.left = Formula(None, None, node)
            elif symbol == "~":
                node.left = Negation(None, symbol, node)
            else:
                node.left = Atom(None, symbol, node)
            return node.left        
        else:
            if symbol == "(":
                node.right = Formula(None, None, node)
            elif symbol == "~":
                node.right = Negation(None, symbol, node)
            else:
                node.right = Atom(None, symbol, node)
            return node.right
    elif symbol in operatorList and symbol != "~":
        while 1:
            node = node.parent
            if node.symbol != "~":
                break
        if symbol == "^":
            node = Conjunction(node)
        elif symbol == "v":
            node = Disjunction(node)
        elif symbol == "=>":
            node = Implication(node)           
        else:
            node = Biconditional(node)
        node.left.parent = node
        if node.parent:
            if not node.parent.symbol or node.parent.symbol == "~":
                node.parent.left = node
            else:
                node.parent.right = node
        return node
    return node

def findRoot(node):
    while 1:
        if node.parent == None:
            break
        else:
            node = node.parent
    if node.symbol == None:
        node = node.left
        node.parent = None

    return node

def getTreeList(RList):
    KBList = []
    for R in RList:
        node = Formula(None)
        for symbol in R:
            node = parseToTree(symbol, node)
        node = findRoot(node)
        KBList.append(node)
    return KBList

def toCNF(node, step):
    if not node: return None
    if step == 0:
        if node.symbol == "<=>":
            parent = node.parent
            if parent != None:
                if parent.left == node:
                    pos = "left"
                else:
                    pos = "right"
            left = copy.copy(node.left)
            right = copy.copy(node.right)
            node = Conjunction(node)
            node.parent = parent
            if parent != None:
                if pos == "left":
                    node.parent.left = node
                else:
                    node.parent.right = node
            node.left = Implication(None, None, node)
            node.right = Implication(None, None, node)
            node = node.left
            node.left = left
            node.left.parent = node
            node.right = right
            node.right.parent = node
            node = node.parent
            node = node.right
            node.left = right
            node.left.parent = node
            node.right = left
            node.right.parent = node
            node = node.parent
    elif step == 1:
        if node.symbol == "=>":
            parent = node.parent
            if parent == None:
                left = copy.copy(node.left)
                node = Disjunction(node)
            else:
                if parent.left == node:
                    pos = "left"
                else:
                    pos = "right"
                left = copy.copy(node.left)
                node = Disjunction(node)
                if pos == "left":
                    node.parent.left = node
                else:
                    node.parent.right = node
            node.left = Negation(None, None, node)
            node.right.parent = node
            node = node.left
            node.left = left
            node.left.parent = node
            node = node.parent            
    elif step == 2:
        if node.symbol == "~":
            if type(node.left) == Negation:
                if node.parent == None:
                    node = node.left.left
                    node.parent = None
                else:

                    if node.parent.left == node:
                        node.parent.left = node.left.left
                    else:
                        node.parent.right = node.left.left
                    parent = node.parent                        
                    node = node.left.left
                    node.parent = parent
                    node = node.parent
                    
            elif type(node.left) == Atom:
                pass
            else:
                parent = node.parent
                if parent != None:
                    if parent.left == node:
                        pos = "left"
                    else:
                        pos = "right"
                node = node.left
                left = copy.copy(node.left)
                right = copy.copy(node.right)
                if type(node) == Conjunction:
                    node = Disjunction(node)
                else: 
                    node = Conjunction(node)
                
                node.parent = parent
                if parent != None:
                    if pos == "left":
                        node.parent.left = node
                    else:
                        node.parent.right = node
                node.left = Negation(None, None, node)
                node.right = Negation(None, None, node)
                left.parent = node.left
                right.parent = node.right
                node.left.left = left
                node.right.left = right               
    elif step == 3:
        if node.symbol == "v" and type(node.left) == Conjunction:
            parent = node.parent
            if parent != None:
                if parent.left == node:
                    pos = "left"
                else: 
                    pos = "right"
            A = copy.copy(node.left.left)
            B = copy.copy(node.left.right)
            C1 = copy.copy(node.right)
            C2 = copy.copy(node.right) 
            node = Conjunction(None, None, parent)
            node.left = Disjunction(None, None, node, A, C1)
            A.parent = node.left
            C1.parent = node.left
            node.right = Disjunction(None, None, node, B, C2)
            B.parent = node.right
            C2.parent = node.right
            if parent != None:
                if pos == "left":
                    node.parent.left = node
                else:
                    node.parent.right = node

        elif node.symbol == "v" and type(node.right) == Conjunction:
            parent = node.parent
            if parent != None:
                if parent.left == node:
                    pos = "left"
                else: 
                    pos = "right"
            A1 = copy.copy(node.left)
            A2 = copy.copy(node.left)
            B = copy.copy(node.right.left)
            C = copy.copy(node.right.right)
            node = Conjunction(None, None, parent)
            node.left = Disjunction(None, None, node, A1, B)
            A1.parent = node.left
            B.parent = node.left
            node.right = Disjunction(None, None, node, A2, C)
            A2.parent = node.right
            C.parent = node.right
            if parent != None:
                if pos == "left":
                    node.parent.left = node
                else:
                    node.parent.right = node

    toCNF(node.left, step)
    toCNF(node.right, step)

    node = findRoot(node)
    return node

def findError(node):
    if not node: return False
    if node.symbol == "v" and (node.left.symbol == "^" or node.right.symbol == "^"):
        return True
    findError(node.left)
    findError(node.right)




