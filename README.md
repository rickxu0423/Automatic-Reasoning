## Automatic-Reasoning

## 1. Modus Ponens:
KB: P,P=>Q
Alpha: Q

## 2. Wumpus Word(Simple):
# KB: 
`~P1-1,B1-1<=>(P1-2vP2-1),B2-1<=>((P1-1vP2-2)vP3-1),~B1-1,B2-1`
# Alpha: 
`P1-2`

## 3. Horn Clauses:
# KB:
`Mythical=>~Mortal, ~Mythical=>(Mortal^Mammal), (~MortalvMammal)=>Horned, Horned=>Magical`
# Alpha:
```
    1.Mythical
    2.Magical
    3.Horned
```

## 4. The Doors of Enlightenment:
(a) Smullyan's problem
# KB: 
`A<=>X, B<=>(YvZ), C<=>(A^B), D<=>(X^Y), E<=>(X^Z), F<=>(DvE), G<=>(C=>F), H<=>((G^H)=>A)`
# Alpha:
```
    1. X
    2. Y
    3. Z
    4. W
```