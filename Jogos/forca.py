import random

def jogar():

    print("*******************************")
    print("Bem-vindo ao jogo da Forca !")
    print("*******************************")

    file = open("words.txt", "r")

    words = []
    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    word_index = random.randrange(0, len(words))

    secret_word = words[word_index]
    secret_word_treatment = secret_word.upper()

    letter_right = ["_" for letter in secret_word_treatment]

    dead = False
    got_it_right = False
    mistakes = 0

    print(letter_right)

    while not dead and not got_it_right:
        guess = input("Escolha uma letra !")
        guess = guess.strip().upper()

        if guess in secret_word_treatment:
            index: int = 0
            for letter in secret_word_treatment:
                if guess == letter:
                    letter_right[index] = guess
                index = index + 1
        else:
            mistakes = mistakes + 1
            draw_forca(mistakes)

        if mistakes == 6:
            dead = True

        if not "_" in letter_right:
            got_it_right = True

        print(letter_right)

    if got_it_right:
        print("Você acertou a palavra, parabéns !!!")
    elif mistakes:
        print("Você foi enforcado, que pena !!!")

    print("Fim de jogo !")

def draw_forca(mistakes):
    print("  _______     ")
    print(" |/      |    ")

    if(mistakes == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(mistakes == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(mistakes == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (mistakes == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    jogar()

