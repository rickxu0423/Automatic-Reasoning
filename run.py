from parser import splitString, getTreeList, getSymbols, toCNF, findError
from modelChecking import modelChecking
from resolution import resolution
from time import time

while 1:
    KB_row = input("Please Enter Knowledge Base(format see README): ")
    if KB_row:
        break
while 1:
    alpha_row = input("Please Enter Alpha(format see README): ")
    if alpha_row:
        break

KB_new = KB_row.split(",")
alpha_new = alpha_row.split(",")

RList = splitString(KB_new)
alphaList = splitString(alpha_new)
symbols = getSymbols(RList, alphaList)

KB = getTreeList(RList)
alpha = getTreeList(alphaList)

t = time()
entail = modelChecking(KB, alpha, symbols, dict())
print("Model Checking Result: ", entail)
print("Calculated in %.1fs" % (time() - t))

clauseSet = set()
for R in KB:
    CNFTree = R
    for i in range(0, 4):
        if i == 2:
            while True:
                CNFTree = toCNF(CNFTree, i) 
                if CNFTree.symbol != "~" or CNFTree.left.symbol != "~":
                    break
        elif i == 3:
            error = True
            while error:
                CNFTree = toCNF(CNFTree, i) 
                error = findError(CNFTree)
        else:
            CNFTree = toCNF(CNFTree, i)
    clauses = CNFTree.generateClauses(set())  
    if type(clauses) != set:
        clauses = {clauses}
    for clause in clauses:
        clauseSet.add(clause)


alphaReverseList = list()
for alpha in alphaList:
    alpha.insert(0, "(")
    alpha.insert(0, "~")
    alpha.append(")")
    alphaReverseList.append(alpha)  
alphaReverse = getTreeList(alphaList)
for alphaReverse in alphaReverse:
    CNFTree = alphaReverse
    for i in range(0, 4):
        if i == 2:
            while True:
                CNFTree = toCNF(CNFTree, i) 
                if CNFTree.symbol != "~" or CNFTree.left.symbol != "~":
                    break
        elif i == 3:
            error = True
            while error:
                CNFTree = toCNF(CNFTree, i) 
                error = findError(CNFTree)
        else:
            CNFTree = toCNF(CNFTree, i)
    clauses = CNFTree.generateClauses(set())
    if type(clauses) != set:
        clauses = {clauses}
    for clause in clauses:
        clauseSet.add(clause)

t = time()
print("Resolution Result: ", resolution(clauseSet))
print("Calculated in %.1fs" % (time() - t))
print(" ")



