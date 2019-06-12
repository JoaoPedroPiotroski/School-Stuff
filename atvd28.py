quantidade_de_cds = int(input("Quantos CDs você tem? \n> "))
preço_total = 0
for i in range(quantidade_de_cds):
    preço = float(input("Qual o preço do %dº CD?\n> "%(i+1)))
    preço_total += preço
print("Cada um custou em média R$" + str(preço_total/quantidade_de_cds))
print("A coleção custou no total R$" + str(preço_total))

