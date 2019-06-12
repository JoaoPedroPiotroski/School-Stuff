quantidade_de_pessoas = int(input("Quantas pessoas tem na turma?\n> "))
soma_das_idades = 0
for i in range(quantidade_de_pessoas):
    idade = int(input("Diga a idade da %dº pessoa: \n> "%(i+1)))
    soma_das_idades += idade
media_das_idades = soma_das_idades / quantidade_de_pessoas
if 0 <= media_das_idades <= 25:
    print("A turma é jovem")
elif 26 <= media_das_idades <= 60:
    print("A turma é adulta")
elif media_das_idades > 60:
    print("A turma é idosa")