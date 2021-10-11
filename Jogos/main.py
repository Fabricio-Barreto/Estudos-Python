import adivinhacao
import forca

print("Escolha seu jogo !")
print("Digite 1 para jogar adivinhação !")
print("Digite 2 para jogar forca !")

game = int(input("Digite o número do jogo !"))

if game == 1:
    adivinhacao.jogar()
elif game == 2:
    forca.jogar()