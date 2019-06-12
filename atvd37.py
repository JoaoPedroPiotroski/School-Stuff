import os
import sys
lista_de_pesos = []
lista_de_alturas = []
maior_peso = 0
codigo = 1
altura_somada = 0
peso_somado = 0
vezes = 0
while codigo != 0 :
    codigo = int(input("Digite seu código: \n> "))
    if codigo != 0 :
        vezes += 1
        peso = float(input("Digite seu peso: \n> "))
        lista_de_pesos.append(peso)
        if peso >= max(lista_de_pesos):
            maior_peso = str("Cliente mais gordo: \n" + str(codigo) + "\n" + str(peso) + "Kg")
        if peso <= min(lista_de_pesos):
            menor_peso = str("Cliente mais magro: \n" + str(codigo) + "\n" + str(peso) + "Kg")
        altura = float(input("Digite sua altura: \n> "))
        lista_de_alturas.append(altura)
        if altura >= max(lista_de_alturas):
            maior_altura = str("Cliente mais alto: \n" + str(codigo) + "\n" + str(altura) + "m")
        elif altura <= min(lista_de_alturas):
            menor_altura = str("Cliente mais baixo: \n" + str(codigo) + "\n" + str(altura) + "m")
        altura_somada += altura
        peso_somado += peso
os.system('cls')
media_altura = altura_somada / vezes
media_peso = peso_somado / vezes
print(menor_altura)
print(maior_altura)
print(menor_peso)
print(maior_peso)
print("A média de altura é: \n %.2f m"%media_altura)
print("A média de peso é: \n %.2f Kg"%media_peso)
