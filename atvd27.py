turmas = int(input("Quantas turmas tem? \n> "))
total = 0
for i in range(turmas):
    numero_de_alunos = int(input("Quantos alunos há na turma %d?\n> "%(i+1)))
    while 0 > numero_de_alunos or numero_de_alunos > 40:
        print("O numero deve ser menor que 40")
        numero_de_alunos = int(input("Quantos alunos há na turma %d?\n> "%(i+1)))
    total += numero_de_alunos
media = total / turmas
print("A média de alunos por turma é %d"%media)