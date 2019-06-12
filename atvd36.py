a=int(input("Qual tabuada você quer ver? "))
b = int(input("Qual o primeiro numero?\n> "))
d = int(input("Qual o segundo numero?\n> "))
while d < b:
    d = int(input("O numero final deve ser maior que o inicial\n> "))
print("a. Montas a tabuada de: %d"%a)
print("Começar por: %d"%b)
print("Terminar em: %d"%d)
if 0 < a <= 10:
    for i in range(b,d+1):
        if i > 0:
            c=i*a
            print("%d X %d = %d"%(a, (i), c))
input()
