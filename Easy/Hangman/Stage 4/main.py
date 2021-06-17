import random

words = ['python', 'java', 'kotlin', 'javascript']
keyword = random.choice(words)
first_three_letters = keyword[0:3]
x = '-' * (len(keyword) - 3)
print("H A N G M A N")
word = str(input("Guess the word: " + first_three_letters + x))
if word == keyword:
    print("You survived!")
else:
    print("You are hanged!")