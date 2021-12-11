def game_grid(matrix_):
    print("---------")
    print("|", *matrix_[0], "|")
    print("|", *matrix_[1], "|")
    print("|", *matrix_[2], "|")
    print("---------")


def check_win(grid):
    col_list = [[j[i] for j in grid] for i in range(3)]
    diagonal_list = [[grid[i][i] for i in range(3)]] + [[grid[i][2 - i] for i in range(3)]]
    matrix_ = grid + col_list + diagonal_list
    return matrix_


def switch_player(move):
    if move % 2 == 0:
        return "X"
    return "O"


def main():
    move = 0
    running = True
    matrix = []
    row_list = [[" " for _ in range(i, i + 3)] for i in range(0, 7, 3)]
    game_grid(row_list)
    win_x = ['X', 'X', 'X']
    win_o = ['O', 'O', 'O']

    while running:
        try:
            i, j = input("Enter the coordinates: ").split()
            i, j = int(i), int(j)
            if 1 <= i <= 3 and 1 <= j <= 3:
                if " " in row_list[i - 1][j - 1]:
                    row_list[i - 1][j - 1] = switch_player(move)
                    game_grid(row_list)
                    move += 1
                    matrix += check_win(row_list)
                    if win_o in matrix:
                        print("O wins")
                        running = False
                    elif win_x in matrix:
                        print("X wins")
                        running = False
                    elif move >= 9:
                        print("Draw")
                        running = False
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")


if __name__ == '__main__':
    main()
