n=123
print(f"{n:.2f}") #respeita casa decimal
print(f"{n:0<10}") #preenche com 0 até 10 casas
print(f"{n:0>10.2f}") #respeita casa decimal/preenche com 0 até 10 casas
print(f"{n:0^10}") #arrodea com 0 até 10 casas
novonum= "{:#>20}".format(n)
print(novonum)

#####

cantor = "John Mackletson, Guitarra Humana e Zubumafu"
print(cantor[0:2])
print(cantor[10:])
print(cantor[:10])
