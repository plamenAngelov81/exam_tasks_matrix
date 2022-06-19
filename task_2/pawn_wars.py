
position_row = {
    0: "8",
    1: "7",
    2: "6",
    3: "5",
    4: "4",
    5: "3",
    6: "2",
    7: "1",
}
positions_col = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}

size = 8
board = []
white_row = 0
white_col = 0
black_row = 0
black_col = 0

for row in range(size):
    current_row = input().split(" ")
    for col in range(size):
        if current_row[col] == "w":
            white_row = row
            white_col = col
        elif current_row[col] == "b":
            black_row = row
            black_col = col
    board.append(current_row)

while True:
    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {positions_col[white_col]}{position_row[white_row]}.")
        break
    elif white_row > 0:
        if white_col - 1 >= 0:
            if board[white_row - 1][white_col - 1] == "b":
                print(f"Game over! White win, capture on {positions_col[black_col]}{position_row[black_row]}.")
                break
        if white_col + 1 < size:
            if board[white_row - 1][white_col + 1] == "b":
                print(f"Game over! White win, capture on {positions_col[black_col]}{position_row[black_row]}.")
                break
    white_row -= 1
    board[white_row][white_col] = "w"

    if black_row == size - 1:
        print(f"Game over! Black pawn is promoted to a queen at {positions_col[black_col]}{position_row[black_row]}.")
        break
    elif black_row < size:
        board[black_row][black_col] = "b"
        if black_col - 1 >= 0:
            if board[black_row + 1][black_col - 1] == "w":
                print(f"Game over! Black win, capture on {positions_col[white_col]}{position_row[white_row]}.")
                break
        if black_col + 1 < size:
            if board[black_row + 1][black_col + 1] == "w":
                print(f"Game over! Black win, capture on {positions_col[white_col]}{position_row[white_row]}.")
                break
    black_row += 1
    board[black_row][black_col] = "b"
