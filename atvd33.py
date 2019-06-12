import textwrap
print("Digite 'Parar' para parar")
temperatura = '0'
x= 0
temperatura_total = 0
temperaturas = []
while temperatura.lower() != 'parar':
    x += 1
    temperatura = input("Temperatura " + str(x) + ": ")
    if temperatura.lower() != 'parar':
        temperaturas.append(float(temperatura))
        temperatura_total += float(temperatura)
print("A menor temperatura foi: %d"%min(temperaturas))
print("A maior temperatura foi: %d"%max(temperaturas))
media = temperatura_total / (x-1)
print("A temperatura média foi: %.2f"%(media))