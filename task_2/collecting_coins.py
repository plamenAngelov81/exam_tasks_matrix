from math import floor


def next_position(x, y, word):
    if word == "up":
        return x - 1, y
    if word == "down":
        return x + 1, y
    if word == "left":
        return x, y - 1
    if word == "right":
        return x, y + 1


def is_inside(x, y, num):
    return 0 <= x < num and 0 <= y < num


def opposite_side(x, y, direction, number):
    if direction == "up":
        return number - 1, y
    if direction == "down":
        return 0, y
    if direction == "left":
        return x, number - 1
    if direction == "right":
        return x, 0


size = int(input())

matrix = []

for _ in range(size):

    matrix.append([x for x in input().split()])

player_row = 0
player_col = 0

for row in range(size):
    condition = False
    for col in range(size):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col
            condition = True
            break
    if condition:
        break

player_path = [[player_row, player_col]]
coins = 0
win_condition = False
command_list = ["up", "left", "down", "right"]
while True:
    command = input()
    if command not in command_list:
        continue
    next_row, next_col = next_position(player_row, player_col, command)
    if is_inside(next_row, next_col, size):
        if matrix[next_row][next_col] != "P" and matrix[next_row][next_col] != "X":
            coins += int(matrix[next_row][next_col])
            matrix[next_row][next_col] = "P"
            player_path.append([next_row, next_col])
        elif matrix[next_row][next_col] == "P":
            player_path.append([next_row, next_col])
        elif matrix[next_row][next_col] == "X":
            player_path.append([next_row, next_col])
            coins = floor(coins - coins * 0.5)
            break
        player_row, player_col = next_row, next_col
    else:
        exit_row, exit_col = opposite_side(next_row, next_col, command, size)
        if matrix[exit_row][exit_col] != "P" and matrix[exit_row][exit_col] != "X":
            coins += int(matrix[exit_row][exit_col])
            matrix[exit_row][exit_col] = "P"
            player_path.append([exit_row, exit_col])
        elif matrix[exit_row][exit_col] == "P":
            player_path.append([exit_row, exit_col])
        elif matrix[exit_row][exit_col] == "X":
            player_path.append([exit_row, exit_col])
            coins = floor(coins - coins * 0.5)
            break
        player_row, player_col = exit_row, exit_col
    if coins >= 100:
        win_condition = True
        break

if win_condition:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print("Your path:")
for k in player_path:
    print(k)
