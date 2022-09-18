import aditivo

#print(aditivo.complemento)
numeroAbaco = input("Digite um número: ")
tamanhoAbaco = len(numeroAbaco)
unidades = ["PlaceHolder", "Unidades", "Dezenas", "Centenas",
            "Milhares", "Milhões", "Bilhões", "Trilhões",
            "Quadrilhões", "Quintilhões", "Sextilhões",
            "Septilhões", "Octilhão", "Nonilhão", "Decilhão"]

print("")
print("Seus números (num àbaco) são:")

for i in numeroAbaco:
    print(i , unidades[tamanhoAbaco])
    tamanhoAbaco = tamanhoAbaco - 1
else:
    print("")
    print("Fim de Loop ^-^")


