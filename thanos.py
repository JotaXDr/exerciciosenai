
import random, os  

esconde = random.randrange (0,50)

dificuldade = int(input(" 1-Easy \n 2-Medium \n 3-Hard \n R: "))
acertou = False

if dificuldade == 1:
    tentativas = 15
elif dificuldade == 2:
    tentativas = 10
else:
    tentativas = 5

for x in range (0, tentativas) :
    print("Você tem " + str(x + 1) + " de " + str(tentativas) + " tentativas")

    nt = int (input("Informe um numero: "))
    if nt > esconde:
        print("Esta mais a esquerda")
    elif nt < esconde: 
        print("Esta mais para a direita")
    else: 
        acertou = True
        break

if acertou == False:
    print("Você perdeu ele está na posição " + str(esconde))
else:
    print("Achou!")


