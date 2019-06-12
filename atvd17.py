n=int(input("Numero: "))
fatorial=1
for i in range(1,n+1):
    fatorial = fatorial * i
print("A fatorial de " + str(n) + ' é:\n')
print(fatorial)
input()