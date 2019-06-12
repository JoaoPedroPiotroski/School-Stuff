a=int(input("Qual tabuada você quer ver? "))
print("a. Tabuada de %d"%a)
if 0 < a <= 10:
    for i in range(11):
        if i > 0:
            c=i*a
            print(c)
input()
