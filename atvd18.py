condition = True

soma = 0
numero = []

while condition:
    num=int(input('Digite o numero: '))
    
    if (num) != 0:
        soma += (num)
        numero.append(num)
    else:
        break
print('Soma: ' +str(soma))
print('menor valor: %d' %(min(numero)))
print('maior valor: %d' %(max(numero)))
input()