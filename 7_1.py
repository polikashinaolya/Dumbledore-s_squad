game_board_new = {number: number for number in range(1, 10)}
No = 'N'


def correct_number(game_board, number):
    return game_board[number] == number


def con_of_human(game_board, number):
    game_board[number] = 'X'


def con_of_comp(game_board):
    for number in range(1, 10):
        if correct_number(game_board, number):
            game_board[number] = 'O'
            break


def print_board(game_board):
    print(game_board[1], game_board[2], game_board[3])
    print(game_board[4], game_board[5], game_board[6])
    print(game_board[7], game_board[8], game_board[9])


while No == 'N':
    print_board(game_board_new)
    print('Введите номер ячейки')
    number_new = int(input())
    if not correct_number(game_board_new, number_new):
        while not correct_number(game_board_new, number_new):
            print('Введите другой номер')
            number_new = int(input())
    con_of_human(game_board_new, number_new)
    con_of_comp(game_board_new)
    print_board(game_board_new)
    print('Это конец игры?(Y/N)')
    No = input()

