print("Digite um número para o àbaco!")
num = int(input())

if (num > 0) and (num < 10):
    print("Seu número",num, "é uma unidade :)")
    
elif (num > 9) and (num < 100):
    print("Seu número",num, "é uma dezena :)")
    
elif (num > 99) and (num < 1000):
    print("Seu número",num, "é uma centena :)")
    
elif (num > 999):
    print("Seu número",num, "é um milhar à diante! :)")
    
else :
    print("Seu número é vazio, ou inválido :(")
