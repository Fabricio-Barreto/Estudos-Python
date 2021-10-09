import random

print("*********************************")
print("Bem Vindo ao jogo da adivinhação!")
print("*********************************")

secret_number = random.randrange(1,101)
score = 1000

print("Qual o nível de dificuldade ?")
print("Digite 1 para Fácil - 10 tentativas")
print("Digite 2 para Médio - 5 tentativas")
print("Digite 3 para Dífícil - 3 tentativas")
while(True):
    difficulty = int(input("Qual será o nível ? "))

    if difficulty == 1:
        number_of_difficulty = 10
        score_loss_multiple = 25
        print("Você escolheu a dificuldade Fácil !")
        print("***************************************")
        break
    elif difficulty == 2:
        number_of_difficulty = 5
        score_loss_multiple = 50
        print("Você escolheu a dificuldade Médio !")
        print("***************************************")
        break
    elif difficulty == 3:
        number_of_difficulty = 3
        score_loss_multiple = 100
        print("Você escolheu a dificuldade Difícil !")
        print("***************************************")
        break

attempt = 0

while(attempt < number_of_difficulty):
    score = score - attempt * score_loss_multiple
    attempt = attempt + 1
    print("Tentativa:", attempt)
    guess = int(input("Digite o seu Número entre 1 a 100: "))

    print("Você digitou ", guess)

    if secret_number == guess:
        print("Você acertou !!!")
        print("***************************************")
        break
    elif secret_number > guess:
        print("O número secreto é MAIOR que o seu chute")
    else:
        print("O número secreto é MENOR que o seu chute")

    print("***************************************")

print("Você acertou em {} Tentativa(s)".format(attempt))
print("Sua Pontuação foi de {}".format(score))
print("Fim de jogo !")