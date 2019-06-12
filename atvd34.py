print("Ver solução da 21")
a = int (input ("Numero\n>"))
if a > 1 : 
    for i in range(2,a):
        if a % i == 0:
            print("O número não é primo")
            break
        else:
            print("O número é primo")
else:
    print("O número não é primo")
