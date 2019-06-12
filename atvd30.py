preço = float(input("Preço do pão:\n> "))
print("a. Preço do pão: R$ %.2f" %preço )
print("Panificadora Pão de Ontem - Tabela de Preços")
for i in range(50):
    print("%d - R$ %.2f"%(i+1, (i+1)*preço))
