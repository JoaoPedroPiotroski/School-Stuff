pares = 0
impares = 0
for i in range(10):
    numero = int(input("Diga um numero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Tem " + str(pares) + " Números pares")
print("Tem " + str(impares) + " Números impares")