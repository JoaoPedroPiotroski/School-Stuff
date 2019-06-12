soma_de_carros = 0
acidentess = []
firsttime = True
Media_possivel = False
for i in range(5):
    codigo = int(input("Código da cidade %d:\n> "%(i+1)))
    carros = int(input("Quantos carros  há na cidade %d  (em 1999)?\n> "%(i+1)))
    acidente = int(input("Quantos acidentes com vítimas ocorreram na cidade %d (em 1999)?\n> "%(i+1)))
    acidentess.append(acidente)
    if acidente >= max(acidentess):
        maior_indice_de_acidentes = acidente
        cidade_maior = codigo
    elif acidente <= min(acidentess):
        menor_indice_de_acidentes = acidente
        cidade_menor = codigo
    soma_de_carros += carros
    if carros < 2000:
        Media_possivel = True
        if firsttime:
            soma_de_acidentes = 0
            firsttime = False
            contagem = 0
        soma_de_acidentes += acidente
        contagem += 1
print("A maior quantidade de acidentes foi em %d com %d acidentes"%(maior_indice_de_acidentes, cidade_maior))
print("A menor quantidade de acidentes foi em %d com %d acidentes"%(menor_indice_de_acidentes, cidade_menor))
print("A média de carros entre todas as cidades é %.2f"%(float((soma_de_carros/5))))
if Media_possivel:
    print("A média de acidentes em cidades com menos de 2000 veículos de passeio foi %.2f"%(float(soma_de_acidentes/contagem)))

