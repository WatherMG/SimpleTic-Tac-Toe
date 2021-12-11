def game_grid(matrix_):
    print("---------")
    print("|", *matrix_[0], "|")
    print("|", *matrix_[1], "|")
    print("|", *matrix_[2], "|")
    print("---------")


user_input = input()
game_states = {
    "1": "Game not finished",
    "2": "Draw",
    "3": "X wins",
    "4": "O wins",
    "5": "Impossible"}
win_x = ['X', 'X', 'X']
win_o = ['O', 'O', 'O']
count_x = user_input.count("X")
count_o = user_input.count("O")
row_list = [[j for j in user_input[i:i + 3]] for i in range(0, 7, 3)]
col_list = [[j for j in user_input[i::3]] for i in range(3)]
diagonal_list = [[row_list[i][i] for i in range(3)]] + [[row_list[i][2 - i] for i in range(3)]]
matrix = row_list + col_list + diagonal_list
game_grid(row_list)

valid = False
while not valid:
    try:
        i, j = input("Enter the coordinates: ").split()
        i, j = int(i), int(j)
        if 1 <= i <= 3 and 1 <= j <= 3:
            if "_" in row_list[i - 1][j - 1]:
                row_list[i - 1][j - 1] = "X"
                game_grid(row_list)
                valid = True
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    except ValueError:
        print("You should enter numbers!")

# if (win_o in matrix and win_x in matrix) or abs(count_o - count_x) > 1:
#     print(game_states.get("5"))
# elif win_o in matrix:
#     print(game_states.get("4"))
# elif win_x in matrix:
#     print(game_states.get("3"))
# elif "_" in user_input:
#     print(game_states.get("1"))
# else:
#     print(game_states.get("2"))
