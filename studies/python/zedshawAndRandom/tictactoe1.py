def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''

    while not (marker == 'X' or marker == '0'):
        marker = input('Player 1: Do you want to be X or 0?').upper()

    if marker == 'X':
        return ('X', '0')
    else:
        return ('0', 'X')

#  function that takes in the board list object, a marker ('X' or 'O'),
#  and a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

# check if space on board is available
def space_check(board, position):
    return board[position] == ' '  # returns boolean value


# check if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: 1 -9'))

        return position


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'



def replay():
    return input('do wanna replay?').lower().startswith('y')

print('orayt tic tac toe')
while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first.')

    play_game = input('play Yes or No? ')
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("you win orayt")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('draw')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):

                display_board(theBoard)
                print('player 2 won')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('drawww')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break