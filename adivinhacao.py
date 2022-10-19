import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")

    numero_secreto = round(random.randrange(1, 101))
    total_de_tentativas = 0
    total_de_niveis = [1, 2, 3]
    pontos = 1000

    dict_total_de_niveis={}

    dict_total_de_niveis[1] = 20
    dict_total_de_niveis[2] = 10
    dict_total_de_niveis[3] = 5

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel_escolhido = int(input("Defina o nível: "))

    try:
        total_de_tentativas = dict_total_de_niveis[nivel_escolhido]
    except:
        print('erro')

    total_de_tentativas = int(total_de_tentativas)

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("VOCÊ ACERTOU E FEZ {} PONTOS!".format(pontos))
            break
        else:
            if(maior):
                print("você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("Fim do Jogo!")
    print("O número secreto é", numero_secreto)

if(__name__ == "__main__"):
    jogar()