import random
# global variables
theBoard = [' '] * 10  # a list of empty spaces
available = [str(num) for num in range(0, 10)]  # a list of comprehension
players = [0, 'X', '0']  # players[1] == 'X' ; players[-1] == '0'

def display_board(a, b):
    print(f'Available   TIC-TAC-TOE\n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n  -----        -----\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n  -----        -----\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')


def place_marker(avail, board, marker, position):
    board[position] = marker
    avail[position] = ' '


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or  # across the top
            (board[4] == board[5] == board[6] == mark) or  # across the middle
            (board[1] == board[2] == board[3] == mark) or  # across the bottom
            (board[7] == board[4] == board[1] == mark) or  # down the middle
            (board[8] == board[5] == board[2] == mark) or  # down the middle
            (board[9] == board[6] == board[3] == mark) or  # down the right side
            (board[7] == board[5] == board[3] == mark) or  # diagonal
            (board[9] == board[5] == board[1] == mark))  # diagonal

def random_player():
    return random.choice((-1, 1))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board[1:]


def player_choice(board, player):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        try:
            position = int(input('player %s, choose position 1-9 '%(player)))
        except:
            print('try again')
    return position


def replay():
    return input('restart, y or n? ').lower().startswith('y')


while True:
    print('tic tac toe yooo')

    toggle = random_player()
    player = players[toggle]
    print('player %s first' %(player))

    game_on = True
    input('hit enter to continue')
    while game_on:
        display_board(available, theBoard)
        position = player_choice(theBoard, player)
        place_marker(available, theBoard, player, position)

        if win_check(theBoard, player):
            display_board(available, theBoard)
            print('player ' + player + ' wins')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(available, theBoard)
                print('draw')
                break
            else:
                toggle *= -1
                player = players[toggle]


    theBoard = [' '] * 10
    available = [str(num) for num in range(0, 10)]

    if not replay():
        break
