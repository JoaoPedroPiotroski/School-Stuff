wantstorepeat=1
while wantstorepeat==1:
    a=int(input("População do pais menor"))
    b=int(input("População do pais maior"))
    while b < a:
        print("primeiro pais tem que ser menor que o segundo")
        a=int(input("População do pais menor"))
        b=int(input("População do pais maior"))
    ta=int(input("Taxa de crescimento do primeiro pais"))
    tb=int(input("Taxa de crescimento do segundo pais"))
    while ta < tb:
        print("a primeira taxa tem que ser maior que a segunda")
        ta=int(input("Taxa de crescimento do primeiro pais"))
        tb=int(input("Taxa de crescimento do segundo pais"))
    ta=ta/100
    tb=ta/100
    c=0
    while a < b:
        a+=a*ta
        b+=b*tb
        c+=1
    print("demoraram %d anos para se igualarem"%c)


    wantstorepeat=int(input("quer continuar? 1 ou 0? "))
input()