# Automatic-Reasoning

Use command: `python3 run.py` to run the program.\
The first prompt asks you to input the **Knowledge Base** which should be separated by `,` \
The second prompt asks you to input the **Alpha**

**Please have fun with it!**

## Operators:
1. Negation: `~`
2. Conjunction: `^`
3. Disjunction: `v`
4. Implication: `=>`
5. Biconditional: `<=>`
6. Atom: `A or P1-2 or Mythical` is acceptable, but should not include any symbol includes: `'~', ',', 'v', '^', '=', '<', '>'`
Should not include any **space** when you type into logic sentences\
Beacuse the project uses **Binary Tree**, please always add **brackets**!
## Input Example:
`(Av~BvC)=>D,A^B^C` should be writen as: `((Av~B)vC)=>D,(A^B)^C`

## Exercises:
### 1. Modus Ponens:
**KB:**
```
P,P=>Q
```
**Alpha:**
```
Q
```

### 2. Wumpus Word(Simple):
**KB:**
```
~P1-1,B1-1<=>(P1-2vP2-1),B2-1<=>((P1-1vP2-2)vP3-1),~B1-1,B2-1
```
**Alpha:**
```
P1-2
```

### 3. Horn Clauses:
**KB:**
```
Mythical=>~Mortal, ~Mythical=>(Mortal^Mammal), (~MortalvMammal)=>Horned, Horned=>Magical
```
**Alpha:**
```
Mythical
Magical
Horned
```

### 4. The Doors of Enlightenment:
**(a) Smullyan's problem** \
\
**KB:** 
```
A<=>X, B<=>(YvZ), C<=>(A^B), D<=>(X^Y), E<=>(X^Z), F<=>(DvE), G<=>(C=>F), H<=>((G^H)=>A)
```
**Alpha:**
```
X
Y
Z
W
```
**(b) Liu's problem** \
\
**KB:**
```
A<=>X,H<=>((G^H)=>A),C<=>(A^M),G<=>(C=>N)
```
**Alpha:**
```
X
Y
Z
W
```
