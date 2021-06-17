import random
word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")

while True:
    decision = input('Type "play" to play the game, "exit" to quit: ')
    if decision == "play":
        correct_word = random.choice(word_list)
        hidden = list("-"*len(correct_word))
        guessed = list()
        opportunities = 8
        while opportunities > 0:
            print()
            print("".join(hidden))
            letter = input("Input a letter: ")
            if len(letter) != 1:
                print("You should input a single letter")
            elif not letter.islower():
                print("It is not an ASCII lowercase letter")
            elif letter in guessed:
                print("You already typed this letter")
            elif letter in correct_word:
                guessed.append(letter)
                for i in range(len(correct_word)):
                    if correct_word[i] == letter:
                        hidden[i] = letter
            else:
                guessed.append(letter)
                print("No such letter in the word")
                opportunities -= 1

            if "".join(hidden) == correct_word:
                print(f"You guessed the word {correct_word}!")
                print("You survived!\n")
                break
        else:
            print("You are hanged!")
    elif decision == "exit":
        break




