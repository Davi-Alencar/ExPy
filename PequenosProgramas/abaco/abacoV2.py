import aditivo

#print(aditivo.complemento)
numeroAbaco = input("Digite um número: ")
tamanhoAbaco = len(numeroAbaco)
unidades = ["PlaceHolder", "Unidades", "Dezenas", "Centenas",
            "Milhares", "Milhões", "Bilhões", "Trilhões",
            "Quadrilhões", "Quintilhões", "Sextilhões",
            "Septilhões", "Octilhão", "Nonilhão", "Decilhão"]

unidades2 = ["Unidades de ", "Dezenas de ",
             "Centenas de",]


for x in unidades:
    for y in unidades2:

##        if(x in unidades[0,1,2,3])
##        if (x == unidades[range(0, 5)]):
#        if ((x == unidades[0]) or (x == unidades[1])
#        or (x == unidades[2]) or (x == unidades[3])):
        if (x in unidades[:4]):
            pass
        else:
            print(y, x)


print("")
print("Seus números (num àbaco) são:")

for i in numeroAbaco:
    print(i , unidades[tamanhoAbaco])
    tamanhoAbaco = tamanhoAbaco - 1
else:
    print("")
    print("Fim de Loop ^-^")


