import sys
import time
lista_de_alturas = []
for i in range(10):
    numero = int(input("Número do aluno: \n> "))
    altura = float(input("Altura do aluno em centímetros: \n> "))
    lista_de_alturas.append(altura)
    if altura >= max(lista_de_alturas):
        maior_aluno_ = numero
        maior_aluno_altura = altura
    elif altura <= min(lista_de_alturas):
        menor_aluno_ = numero
        menor_aluno_altura = altura
aluno_mais_alto = ("Aluno mais alto: \nNúmero: %d \nAltura: %.1f cm\n"%(maior_aluno_, maior_aluno_altura))
aluno_mais_baixo = ("Aluno mais baixo: \nNúmero: %d \nAltura: %.1f cm"%(menor_aluno_, menor_aluno_altura))
for character in aluno_mais_alto:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)
for character in aluno_mais_baixo:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    
