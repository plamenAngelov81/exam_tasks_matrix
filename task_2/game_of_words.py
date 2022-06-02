def position(x, y, word):
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


some_string = list(input())
size = int(input())

matrix = []

for _ in range(size):
    data = input()
    matrix.append([data[x] for x in range(len(data))])

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

number_of_commands = int(input())

for i in range(number_of_commands):
    matrix[player_row][player_col] = "-"
    command = input()
    next_row, next_col = position(player_row, player_col, command)
    if is_inside(next_row, next_col, size):
        player_row, player_col = next_row, next_col
        if matrix[next_row][next_col] != "-":
            some_string.append(matrix[next_row][next_col])
            matrix[next_row][next_col] = "P"
    else:
        matrix[player_row][player_col] = "P"
        some_string.pop()

print(f"{''.join(some_string)}")
for j in matrix:
    print(*j, sep="")
