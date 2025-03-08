import adivinhacao
import chatbot
import imc

def escolhe_jogo():
    print("***********************************")
    print("*Escolha o seu jogo!*")
    print("***********************************")

    print("(1)Adivinhação  (2)Chatbot  (3)IMC")

    jogo = int(input("Qual jogo?"))

    if (jogo == 1):
        print("Jogando adivinhação")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando chatbot")
        chatbot.jogar()
    else:
        print("Jogando IMC")
        imc.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
