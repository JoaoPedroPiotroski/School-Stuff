A=80000
B=200000
C=0
while A < B:
    C+=1
    A+=A*0.03
    B+=B*0.015
if A >= B:
    print("Demoraram %d anos para se igualarem"%C)
input()