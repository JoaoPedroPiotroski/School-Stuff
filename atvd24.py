quantidade_de_notas = int(input("Quantas notas você quer testar?\n> "))
notas = 0
for i in range(quantidade_de_notas):
    nota=float(input("Digite uma nota\n> "))
    notas += nota
media = notas / quantidade_de_notas
print("A média é: " + str(media) + ".")

    