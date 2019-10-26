from parser import splitString, getTreeList, getSymbols, toCNF, CNFTree_print
from modelChecking import modelChecking
from resolution import resolution
from time import time

KB_row = input("Please Enter Knowledge Base(format see README): ")
alpha_row = input("Please Enter Alpha(format see README): ")

KB_new = KB_row.split(",")
alpha_new = alpha_row.split(",")

RList = splitString(KB_new)
alphaList = splitString(alpha_new)
symbols = getSymbols(RList, alphaList)

KB = getTreeList(RList)
alpha = getTreeList(alphaList)

t = time()
entail = modelChecking(KB, alpha, symbols, dict())
print(" ")
print("Model Checking Result: ", entail)
print("Calculated in %.1fs" % (time() - t))
print(" ")

clauseSet = set()
for R in KB:
    CNFTree = R
    for i in range(0, 4):
        if i == 2:
            while True:
                CNFTree = toCNF(CNFTree, i) 
                if CNFTree.symbol != "~" or CNFTree.left.symbol != "~":
                    break
        else:
            CNFTree = toCNF(CNFTree, i)
    clauses = CNFTree.generateClauses(set())
    for clause in clauses:
        if type(clause) != frozenset:
            clause = clause.split(',')
        clauseSet.add(frozenset(clause))

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
        else:
            CNFTree = toCNF(CNFTree, i)
    clauses = CNFTree.generateClauses(set())
    for clause in clauses:
        if type(clause) != frozenset:
            clause = clause.split(',')
        clauseSet.add(frozenset(clause))

t = time()
print("Resolution Result: ", resolution(clauseSet))
print("Calculated in %.1fs" % (time() - t))
print(" ")



