# Write your code here
import random

words = "python java kotlin javascript".split()  # update to full dictionary later?

print(" ".join("hangman".upper()))

word = random.choice(words)
lives = 8
correct_letters = set()


def generate_display_word():
    display_word = ""
    for letter in word:
        if letter.lower() in correct_letters:
            display_word += letter
        else:
            display_word += "-"
    return display_word


def guess():
    global lives
    print()
    print(generate_display_word())
    letter = input("Input a letter: ").lower()
    if letter in word:
        if letter in correct_letters:
            print("No improvements")
        else:
            correct_letters.add(letter)
            return  # prevent decrementing lives
    else:
        print("No such letter in the word")
    lives -= 1


while lives > 0:  # and correct_letters != set(word):
    guess()
if generate_display_word() == word:
    print(word, "You guessed the word!", "You survived!", sep="\n")
else:
    print("You are hanged!")
