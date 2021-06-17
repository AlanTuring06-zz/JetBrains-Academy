import random

words = ['python', 'java', 'kotlin', 'javascript']
keyword = random.choice(words)
print("H A N G M A N")
word = str(input("Guess the word: "))
if word == keyword:
    print("You survived!")
else:
    print("You are hanged!")
