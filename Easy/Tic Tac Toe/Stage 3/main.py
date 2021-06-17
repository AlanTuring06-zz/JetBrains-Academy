# write your code here
user_input = input('Enter cells:')
print('---------')
print('| '+ user_input[0] + ' ' + user_input[1]+ ' ' + user_input[2]+ ' '+'|')
print('| '+ user_input[3] + ' ' + user_input[4]+ ' ' +user_input[5]+' '+ '|')
print('| '+ user_input[6]+ ' ' +user_input[7]+ ' '+ user_input[8]+ ' '+'|')
print('---------')
x_num=0
o_num=0
def owin():
    if  user_input[0] == user_input[1] == user_input[2] == 'O':
        return True
    elif user_input[3] == user_input[4] == user_input[5] == 'O':
        return True
    elif user_input[6] == user_input[7] == user_input[8] == 'O':
        return True
    elif user_input[0] == user_input[4] == user_input[8] == 'O':
        return True
    elif user_input[2] == user_input[4] == user_input[6] == 'O':
        return True
    elif user_input[2] == user_input[5] == user_input[8] == 'O':
        return True
    elif user_input[1] == user_input[4] == user_input[7] == 'O':
        return True
    elif user_input[0] == user_input[3] == user_input[6] == 'O':
        return True

def xwin():
    if user_input[0] == user_input[1] == user_input[2] == 'X':
        return True
    elif user_input[3] == user_input[4] == user_input[5] == 'X':
        return True
    elif user_input[6] == user_input[7] == user_input[8] == 'X':
        return True
    elif user_input[0] == user_input[4] == user_input[8] == 'X':
        return True
    elif user_input[2] == user_input[4] == user_input[6] == 'X':
        return True
    elif user_input[2] == user_input[5] == user_input[8] == 'X':
        return True
    elif user_input[1] == user_input[4] == user_input[7] == 'X':
        return True
    elif user_input[0] == user_input[3] == user_input[6] == 'X':
        return True

for i in range(0,9):
    if user_input[i] == 'X':
        x_num += 1
    if user_input[i] == 'O':
        o_num += 1

def draw():
    if owin() is not True and xwin() is not True:
        if "_" not in user_input:
            return True
if draw() is True:
    print("Draw")

def im_possible():
    if owin()is True and xwin() is True or owin()is not True and xwin() is not True and abs (x_num - o_num) >= 2:
        return True

def gnf():
    if xwin() is not True and owin() is not True and im_possible() is not True and "_" in user_input:
        return True
if gnf()is True:
    print('Game not finished')
elif im_possible() is True:
    print('Impossible')
elif owin() is True:
    print('O wins')
elif xwin() is True:
    print('X wins')
