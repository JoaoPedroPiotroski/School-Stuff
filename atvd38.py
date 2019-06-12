salario_inicial = float(input("Qual o salário inicial do funcionário? \n> "))
salario = salario_inicial
ano_final = int(input("Qual o ano atual? \n> "))
aumento_anual = 0.015
while ano_final < 1995:
    ano_final = int(input("Qual o ano atual? \n: "))
''' 
    QUE SALARIO E ESSE O 
'''
vezes = ano_final - 1995
for i in range(vezes):
    salario += salario_inicial * aumento_anual
    aumento_anual = aumento_anual * 2
print("O salário atual do funcionário é: \nR$ %.2f"%salario)