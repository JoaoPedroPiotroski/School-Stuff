
nome=input("Nome: ")
idade=int(input("Idade: "))
salario=float(input("Salario: "))
sexo=input("Sexo: ")
ec=input("Estado civil: ")
while len(nome) <= 3:
    print("Nome tem que ter mais que 3 caracteres:")
    nome=input("Nome: ")
while idade < 0 or idade > 150:
    print("idade entre 0 e 150:")
    idade=int(input("Idade:"))
while salario < 0:
    print("Salario tem que ser maior que 0")
    salario=float(input("salario: "))
while sexo != "m" and sexo != "M" and sexo != "f" and sexo != "F":
    print("Sexo M ou F")
    sexo=str(input("Sexo: "))
while ec != "S" and ec!= "s" and ec!= "C" and ec!= "c" and ec!= "V" and ec!= "v" and ec!= "D" and ec!= "d":
    print("Estado civil deve ser ou S C V ou D")
    ec=input("Estado civil: ")

