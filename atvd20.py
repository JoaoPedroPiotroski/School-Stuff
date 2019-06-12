
import sys
continuar = 1
while continuar == 1:
    n=int(input("Numero: "))
    if 0 < n < 16:
        fatorial=1
        for i in range(1,n+1):
            fatorial = fatorial * i
        print("A fatorial de " + str(n) + ' é:\n')
        print(fatorial)
    else:
        sys.exit
    continuar=int(input("Quer continuar? 1 - Sim | 2 - Não\n>"))
else:
    sys.exit
    