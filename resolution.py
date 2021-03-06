import itertools

def resolution(clauseSet):
    new = set()
    while 1:
        for pair in itertools.combinations(clauseSet, 2):
            m = 0
            Ci = set(pair[0])
            for a in Ci:
                for b in Ci:
                    if a == "~" + b or "~" + b == a:
                        m += 1
            if m > 0:
                m = 0
                continue
            
            Cj = set(pair[1])
            for a in Cj:
                for b in Cj:
                    if a == "~" + b or "~" + b == a:
                        m += 1
            if m > 0:
                m = 0
                continue
            resolvents = check(Ci, Cj)
            if len(resolvents) == 0:
                continue
            for stuff in resolvents:
                if len(stuff) == 0:
                    return True
            new = new.union(resolvents)
        if new.issubset(clauseSet):
            return False
        clauseSet = clauseSet.union(new)
        

def check(Ci, Cj):
    clause = set()
    if len(Ci) > 2 and len(Cj) > 2:
        return clause  
    for i in Ci:
        for j in Cj:
            if i == "~" + j or "~" + i == j:
                Ci_new = set(Ci)
                Ci_new.remove(i)
                Cj_new = set(Cj)
                Cj_new.remove(j)
                clause.add(frozenset(Ci_new.union(Cj_new)))
    return clause
        
