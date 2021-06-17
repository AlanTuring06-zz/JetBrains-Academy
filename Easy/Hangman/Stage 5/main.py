import random

print("H A N G M A N")
print()
words = ['python', 'java', 'kotlin', 'javascript']
keyword = random.choice(words)
time = 0
hidden = '-' * (len(keyword))
while time < 8:
    print(''.join(hidden))
    word = str(input("Input a letter: "))
    if word in keyword:
        for x in range(0,len(keyword)):
            if word == keyword[x]:
                word = hidden[x]
    else:
        print("No such letter in the word")
    print()
    time += 1
print('''Thanks for playing!
We'll see how well you did in the next stage''')
