#PEDRA, PAPEL E TESOURA

print("VAMOS JOGAR PEDRA, PAPEL E TESOURA!")

#IMPORTAR BIBLIOTECA
from random import randint

#DECLARAR VARIÁVEIS
jogador = int(input("CONSIDERE:\n\n0 = PEDRA\n1 = PAPEL\n2 = TESOURA\n\nAGORA, DIGITE SUA ESCOLHA: "))
bot = (randint(0, 2))

#CÓDIGO
print("\nO BOT DIGITOU", bot)
if jogador == bot:
    print("EMPATE")
elif (jogador == 0 and bot == 1) or (jogador == 1 and bot == 2) or (jogador == 2 and bot == 0):
    print("VOCÊ PERDEU!")
else:
    print("VOCÊ GANHOU!")
