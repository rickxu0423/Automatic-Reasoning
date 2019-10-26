def modelChecking(KB, alpha, symbols, model):
    if len(symbols) == 0:
        if checkList(KB, model):
            return checkList(alpha, model)
        else:
            return True
    else:
        p = symbols.pop()
        rest1 = set(symbols)
        rest2 = set(symbols)
        model1 = dict(model)
        model2 = dict(model)
        model1[p] = True
        model2[p] = False


        return modelChecking(KB, alpha, rest1, model1) and modelChecking(KB, alpha, rest2, model2)


def checkList(KB, model):
    #print(model)
    for R in KB:
        if R.calculate(model) == False:
            return False
    return True
        