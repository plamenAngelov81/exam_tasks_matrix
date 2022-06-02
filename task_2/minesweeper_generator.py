import re


def possible_cells(r, c, num):
    cells = [
        [r - 1, c - 1],
        [r - 1, c],
        [r - 1, c + 1],
        [r, c - 1],
        [r, c + 1],
        [r + 1, c - 1],
        [r + 1, c],
        [r + 1, c + 1]
    ]
    surrounding_cells = []
    for x, y in cells:
        if 0 <= x < num and 0 <= y < num:
            surrounding_cells.append([x, y])
    return surrounding_cells


regex = r"[\d]+"
size = int(input())
number_of_bombs = int(input())

field = []

for row in range(size):
    current_row = []
    for col in range(size):
        current_row.append("-")
    field.append(current_row)


for _ in range(number_of_bombs):
    data = input()
    result = re.finditer(regex, data)
    bomb_coord = []
    for i in result:
        bomb_coord.append(int(i.group()))
    bomb_row, bomb_col = bomb_coord
    field[bomb_row][bomb_col] = "*"


for row in range(size):
    for col in range(size):
        if field[row][col] == "*":
            continue
        bomb_counter = 0
        for i in possible_cells(row, col, size):
            a, b = i
            if field[a][b] == "*":
                bomb_counter += 1
        field[row][col] = str(bomb_counter)

for k in field:
    print(*k, sep=" ")
