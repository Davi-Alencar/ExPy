print("")
print("Bem-vindo à S O L E T R A N D O, \
onde soletramos suas palavras!")
print("")


resposta = str(input("Deseja começar SOLETRANDO? (s/n): "))
print("")

while(resposta == "s"):

    print("Escolha um modo de jogo:")
    print("1 - Uma palavra por vez")
    print("2 - Diversas palavras por vez")
    print("")
    modo = int(input("Digite um número: "))

    if (modo == 1):
        print("Modo: 1 - 'Uma palavra por vez' selecionado!")
    
        palavra = str(input("Digite uma palavra: "))

        print("")
        print("Sua palavra é:")
        print("")

        for i in palavra:
            print (i)  
        else:
            print("")
            resposta = str(input("Deseja continuar SOLETRANDO? (s/n): "))
    elif (modo == 2):
        print("Modo: 2 - 'Diversas palavras por vez' selecionado!")

        vezes = int(input("Digite quantas palavras à soletrar: "))
        repeteco = 1
        armazem = []

        while(vezes > 0):
            print("")
            print("Restam", vezes, "palavras..")
            
            palavra = str(input("Digite a "+ str(repeteco) +"a palavra: "))
            repeteco += 1
            vezes -= 1
            armazem.append(palavra)
        else:
            print("")
            print(armazem)
            print("")
            #for i in palavra:
                #print()
            
else:
    print("")
    print("Obrigado por jogar: SOLETRANDO!")
#não esquecer de comentar processo
#append adiciona inputs da var palavras à lista armazém
