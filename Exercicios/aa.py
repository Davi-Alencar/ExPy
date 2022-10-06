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

###

print(ord(A))
print(ord(B))
print(ord(a))
print(ord(1))

print(chr(65))
print(chr(66))
print(chr(97))

print("Caractere 13 é:", chr(13))


listaCantor = ["John Mackletson", "Guitarra Humana", "Zubumafu"]

for nome in listaCantor:
    print("Hello", nome, "venha visitar!")

for nome in rang[10]:
    print("Hello" end="\t")

print("apple">"Apple")
