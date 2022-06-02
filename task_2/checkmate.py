def right_cell(x, y, step):
    return x, y + step


def left_cell(x, y, step):
    return x, y - step


def up_cell(x, y, step):
    return x - step, y


def down_cell(x, y, step):
    return x + step, y


def right_up_cell(x, y, step):
    return x - step, y + step


def right_down_cell(x, y, step):
    return x + step, y + step


def left_up_cell(x, y, step):
    return x - step, y - step


def let_down_cell(x, y, step):
    return x + step, y - step


def is_inside(x, y, num):
    return 0 <= x < num and 0 <= y < num


size = 8

board = []
queens = []
for _ in range(size):
    board.append(list(input().split()))

for row in range(size):
    for col in range(size):
        if board[row][col] == "Q":
            queens.append([row, col])

wining_queens = []
for i in queens:
    queen_row = i[0]
    queen_col = i[1]
    counter = 1
    while True:
        next_row, next_col = right_cell(queen_row, queen_col, counter)
        if is_inside(next_row, next_col, size):
            if board[next_row][next_col] == "K":
                wining_queens.append([queen_row, queen_col])
                counter = 1
                break
            elif board[next_row][next_col] == "Q":
                counter = 1
                break
        else:
            counter = 1
            break
        counter += 1

    while True:
        left_row, left_col = left_cell(queen_row, queen_col, counter)
        if is_inside(left_row, left_col, size):
            if board[left_row][left_col] == "K":
                wining_queens.append([queen_row, queen_col])
                counter = 1
                break
            elif board[left_row][left_col] == "Q":
                counter = 1
                break
        else:
            counter = 1
            break
        counter += 1

    while True:
        up_row, up_col = up_cell(queen_row, queen_col, counter)
        if is_inside(up_row, up_col, size):
            if board[up_row][up_col] == "K":
                wining_queens.append([queen_row, queen_col])
                counter = 1
                break
            elif board[up_row][up_col] == "Q":
                counter = 1
                break
        else:
            counter = 1
            break
        counter += 1

    while True:
        down_row, down_col = down_cell(queen_row, queen_col, counter)
        if is_inside(down_row, down_col, size):
            if board[down_row][down_col] == "K":
                wining_queens.append([queen_row, queen_col])
                counter = 1
                break
            elif board[down_row][down_col] == "Q":
                counter = 1
                break
        else:
            counter = 1
            break
        counter += 1

    while True:
        right_up_row, right_up_col = right_up_cell(queen_row, queen_col, counter)
        if is_inside(right_up_row, right_up_col, size):
            if board[right_up_row][right_up_col] == "K":
                wining_queens.append([queen_row, queen_col])
                counter += 1
                break
            elif board[right_up_row][right_up_col] == "Q":
                counter = 1
                break
        else:
            counter = 1
            break
        counter += 1

    while True:
        right_down_row, right_down_col = right_down_cell(queen_row, queen_col, counter)
        if is_inside(right_down_row, right_down_col, size):
            if board[right_down_row][right_down_col] == "K":
                wining_queens.append([queen_row, queen_col])
                counter += 1
                break
            elif board[right_down_row][right_down_col] == "Q":
                counter = 1
                break
        else:
            counter = 1
            break
        counter += 1

    while True:
        left_up_row, left_up_col = left_up_cell(queen_row, queen_col, counter)
        if is_inside(left_up_row, left_up_col, size):
            if board[left_up_row][left_up_col] == "K":
                wining_queens.append([queen_row, queen_col])
                counter += 1
                break
            elif board[left_up_row][left_up_col] == "Q":
                counter = 1
                break
        else:
            counter = 1
            break
        counter += 1

    while True:
        left_down_row, left_down_col = let_down_cell(queen_row, queen_col, counter)
        if is_inside(left_down_row, left_down_col, size):
            if board[left_down_row][left_down_col] == "K":
                wining_queens.append([queen_row, queen_col])
                counter += 1
                break
            elif board[left_down_row][left_down_col] == "Q":
                counter = 1
                break
        else:
            counter = 1
            break
        counter += 1

if wining_queens:
    for i in wining_queens:
        print(i)
else:
    print("The king is safe!")
