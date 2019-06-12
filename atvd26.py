quantidade_de_eleitores = int(input("Quantos eleitores há?\n> "))
eleitores_1 = 0
eleitores_2 = 0
eleitores_3 = 0
for i in range(quantidade_de_eleitores):
    voto = int(input("Você deseja votar no candidato 1 , 2 ou 3?\n> "))
    if voto == 1:
        eleitores_1 += 1
    elif voto == 2:
        eleitores_2 += 1
    elif voto == 3:
        eleitores_3 += 1
    while voto != 1 and voto != 2 and voto != 3:
        voto = int(input("Você deseja votar no candidato 1 , 2 ou 3?\n> "))
        if voto == 1:
            eleitores_1 += 1
        elif voto == 2:
            eleitores_2 += 1
        elif voto == 3:
            eleitores_3 += 1
print("Eleitores do 1º candidato: " + str(eleitores_1))
print("Eleitores do 2º candidato: " + str(eleitores_2))
print("Eleitores do 3º candidato: " + str(eleitores_3))

