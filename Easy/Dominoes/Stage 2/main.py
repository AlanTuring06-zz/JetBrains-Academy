import random

Dominos = []
for i in range(7):
    for j in range(i, 7):
        Dominos.append([i, j])
stock = []
player = []
computer = []
pairs = [[6, 6], [5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]
snake = []
status = ''


def shuffle():
    global Dominos, player, computer, stock
    random.shuffle(Dominos)
    stock = Dominos[:14]
    player = Dominos[14:21]
    computer = Dominos[21:28]
    return action()


def action():
    global Dominos, player, computer, stock, pairs, status
    if not [a for a in player if a in pairs] and not [a for a in computer if a in pairs]:
        return shuffle()

    if [a for a in player if a in pairs] and [a for a in computer if a in pairs]:
        player_max = max([a for a in player if a in pairs])
        computer_max = max([a for a in computer if a in pairs])
        if player_max > computer_max:
            player.remove(player_max), snake.append(player_max)
            status = 'computer'
        elif computer_max > player_max:
            computer.remove(computer_max), snake.append(computer_max)
            status = 'player'

    elif [a for a in player if a in pairs]:
        player_max = max([a for a in player if a in pairs])
        player.remove(player_max), snake.append(player_max)
        status = 'computer'
    elif [a for a in computer if a in pairs]:
        computer_max = max([a for a in computer if a in pairs])
        computer.remove(computer_max), snake.append(computer_max)
        status = 'player'


def result():
    global Dominos, player, computer, stock, snake, status
    print('=' * 70)
    print('Stock size:', len(stock))
    print('Computer pieces:', len(computer))
    print()
    print(snake[0])
    print()
    for count, item in enumerate(player, 1):
        print(f"{count}:{item}")
    print()
    print("Status: It's your turn to make a move. Enter your command." if status == 'player' else
          "Status: Computer is about to make a move. Press Enter to continue...")


shuffle()
result()
