import os
divida = float(input("Qual o valor da divida?\nR$ "))

parcelas = int(input("Escolha entre 1, 3, 6, 9, 12 parcelas\n> "))
if parcelas == 1:
        juros = 0
elif parcelas == 3:
        juros = 10/100
elif parcelas == 6:
        juros = 15/100
elif parcelas == 9:
        juros = 20/100
elif parcelas == 12:
        juros = 25/100


valor_dos_juros = divida*juros
valor_da_parcela = divida / parcelas
valor_da_divida = divida + valor_dos_juros
os.system('cls')

print("Valor da Dívida | Valor dos Juros | Quantidade de parcelas | Valor da parcela")
print( (str(valor_da_divida) + "           "  + str(valor_dos_juros) + "               " + str(parcelas) +     "                          " +    str(valor_da_parcela)))

    