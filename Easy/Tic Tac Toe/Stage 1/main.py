# write your code here
from random import choice

items = ['X', 'O']
for _i in range(3):
    print(choice(items)+' '+choice(items)+' '+choice(items))