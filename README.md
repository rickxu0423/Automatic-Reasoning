Automatic-Reasoning
==============================

Brief Introduction
------------------------------
This project implemented two inference methods (Model Checking and Resolution) for **Propositional Logic** and demonstrate them on some example problems.

## Key Data Structures:
>>1. Formula:
    We use Binary Tree to represent formula. For example, `A=>(Bv~CvA)` can be represented as:</br>
    ![binary-tree](/images/binary-tree.png)
    </br>
>>2. Models:
    Models are represented as Dictionary which looks like: **{“A”: True, “B”: False, “C”: True}** and such dictionary provides the value to the leaf nodes which are Atoms when calling function **Calculate** during Model Checking which returns value from leaf to node level by level **recursively**.
    </br>
>>3. Clauses:
    Clauses are represented as **Frozenset** which means (KB^~a) is a big set of frozensets. For example: (AvBv~C)^D is represented as: { frozenset({ “A”, “B”, “~C” }), frozenset({ “D” }) }
    </br>
>>4. CNF Formula:
    The same data structure as **Formula**</br>
    Using function **toCNF** to transfer the original formula to CNF one

How to Run Automatic-Reasoning
------------------------------
Use command: `python3 run.py` to run the program.\
The first prompt asks you to input the **Knowledge Base** which should be separated by `,` \
The second prompt asks you to input the **Alpha**

**Please have fun with it!**

Operators
------------------------------
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

Exercises
------------------------------

### 1. Modus Ponens:
**KB:** `P,P=>Q`</br>
</br>
**Alpha:** `Q`</br>
</br>

### 2. Wumpus Word(Simple):

**KB:** `~P1-1,B1-1<=>(P1-2vP2-1),B2-1<=>((P1-1vP2-2)vP3-1),~B1-1,B2-1`</br>
</br>
**Alpha:** `P1-2`</br>
</br>

### 3. Horn Clauses:
>>Desctiption:
    If the unicorn is mythical, then it is immortal, but if it is not mythical, then it is a mortal mammal. If the unicorn is either immortal or a mammal, then it is horned. The unicorn is magical if it is horned.</br>
    (a) Can we prove that the unicorn is mythical?</br>
    (b) Can we prove that the unicorn is magical?</br>
    (c) Can we prove that the unicorn is horned?</br>
    </br>
**KB:** `Mythical=>~Mortal, ~Mythical=>(Mortal^Mammal), (~MortalvMammal)=>Horned, Horned=>Magical`</br>
</br>
**Alpha:** `Mythical` or `Magical` or `Horned`</br>
</br>

### 4. The Doors of Enlightenment:
>>Desctiption:
    There are four doors X, Y , Z, and W leading out of the Middle Sanctum. At least one of them leads to the Inner Sanctum. If you enter a wrong door, you will be devoured by a fierce dragon. Well, there were eight priests A, B, C, D, E, F, G, and H, each of whom is either a knight or a knave. (Knights always tell the truth and knaves always lie.) They made the following statements to the philosopher:</br>
    • A: X isagooddoor.</br>
    • B: AtleastoneofthedoorsY orZ isgood.</br>
    • C: A and B are both knights.</br>
    • D: X and Y are both good doors.</br>
    • E: X and Z are both good doors.</br>
    • F: Either D or E is a knight.</br>
    • G: IfC isaknight,soisF.</br>
    • H: If G and I (meaning H) are knights, so is A.</br>
    </br>

__(a) Smullyan's problem__

**KB:** `A<=>X, B<=>(YvZ), C<=>(A^B), D<=>(X^Y), E<=>(X^Z), F<=>(DvE), G<=>(C=>F), H<=>((G^H)=>A)`</br>
</br>
**Alpha:**: `X` or `Y` or `Z` or `W`</br>
</br>

__(b) Liu's problem__

**KB:** `A<=>X,H<=>((G^H)=>A),C<=>(A^M),G<=>(C=>N)`</br>
</br>
**Alpha:** `X` or `Y` or `Z` or `W`</br>
</br>