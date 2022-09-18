print("Digite um número correspondente à seu departamento!")
print("1 - Marketing")
print("2 - Vendas")
print("")
departamento = int (input("Digite um número: "))

if (departamento == 1):
    print("Você pertence ao prédio A")
elif (departamento == 2):
    print("Você pertence ao prédio B")
else:
    print("Número Inválido")    
