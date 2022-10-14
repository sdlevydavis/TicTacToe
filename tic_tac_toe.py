def create_board():
    board = [
        ['   ', '   ', '   '],
        ['   ', '   ', '   '],
        ['   ', '   ', '   ']
    ]
    return board


def print_board(board):
    print('╔═════╤═════╤═════╗')
    for row in range(0, len(board)):
        print('║ ', end='')
        for col in range(0, len(board[0])):
            if col == len(board[0]) - 1:
                print(board[row][col], '║')
            else:
                print(board[row][col], '│', end=' ')
        if row != len(board) - 1:
            print('╠═════╪═════╪═════╣')
        else:
            print('╚═════╧═════╧═════╝')


def is_winner(board, game_piece, row, col):
    # horizontal win
    if board[row][0] == game_piece and board[row][1] == game_piece and board[row][2] == game_piece:
        return True

    # vertical win
    if board[0][col] == game_piece and board[1][col] == game_piece and board[2][col] == game_piece:
        return True

    # diagonal win 1
    if board[0][0] == game_piece and board[1][1] == game_piece and board[2][2] == game_piece:
        return True

    # diagonal win 2
    if board[2][0] == game_piece and board[1][1] == game_piece and board[0][2] == game_piece:
        return True

    return False


def board_full(board):
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == '   ':
                return False
    return True


def main_loop():
    game_board = create_board()
    print('Welcome to Tic Tac Toe!')
    player_one = input("Enter Player One's Name: ")
    player_two = input("Enter Player Two's Name: ")
    rotate = True

    loop = True
    while loop is True:
        print()
        if rotate:
            print(f"{player_one}'s Turn...")
            game_piece = ' X '
        else:
            print(f"{player_two}'s Turn...")
            game_piece = ' O '

        invalid = True
        while invalid:
            row = input('Enter row (0-2): ')
            try:
                row = int(row)
                if -1 < row < 3:
                    invalid = False
                else:
                    print("Error: not a valid row")
            except ValueError:
                print("Error: not a valid row")
        print()

        invalid = True
        while invalid:
            col = input('Enter column (0-2): ')
            try:
                col = int(col)
                if -1 < col < 3:
                    invalid = False
                else:
                    print("Error: not a valid column")
            except ValueError:
                print("Error: not a valid column")

        while game_board[row][col] != '   ':
            print('Spot Taken!')
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
        game_board[row][col] = game_piece
        print_board(game_board)

        if board_full(game_board):
            print('Game Tied...No Winner')
            new_game = input('Enter (Q) to quit or (R) to restart: ')
            if new_game.upper() == 'R':
                print()
                restart()
            else:
                quit()
        elif is_winner(game_board, game_piece, row, col) is True:
            if rotate:
                print(f'{player_one} Wins!')
            else:
                print(f'{player_two} Wins!')

            new_game = input('Enter (Q) to quit or (R) to restart: ')
            if new_game.upper() == 'R':
                print()
                restart()
            else:
                quit()
        else:
            rotate = not rotate


def restart():
    main_loop()


if __name__ == '__main__':
    main_loop()
