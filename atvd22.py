a = int (input ("Numero\n>"))
divisiveis = []
Primo = True
if a > 1 : 
    for i in range(2,a):
        if a % i == 0:
            divisiveis.append(i)
            Primo = False
else:
    Primo = True
if Primo == True:
    print("O numero é primo")
elif Primo == False:
    print("O número não é primo")
    print("O número é divisivel por: " + str(divisiveis))
