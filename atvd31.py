preço = 1
x = 0
total = 0
print("a. Lojas Tabajara")
while preço != 0:
    x += 1
    preço = float(input("Produto %d :"%x))
    print("Produto " + str(x) + " : R$" + str(preço) )
    total += preço
print("Total = R$ " + str(total))
dinheiro = float(input("Quanto dinheiro o cliente deu?\n> "))
print("Dinheiro = R$ " + str(dinheiro))
print("Troco = R$ " + str(dinheiro-total))