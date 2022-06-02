

rows, cols = list(map(int, input().split(", ")))

matrix = []
decorations = 0
gifts = 0
cookies = 0
items = 0
condition = False
for row in range(rows):
    matrix.append(list(input().split()))

player_rol = 0
player_col = 0

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == "Y":
            player_rol, player_col = i, j
        if matrix[i][j] in "CDG":
            items += 1
command = input().split("-")
while True:
    if command[0] == "End":
        break
    if command[0] == "right":
        step = int(command[1])
        while True:
            if items == 0:
                condition = True
                break
            if step == 0:
                break
            matrix[player_rol][player_col] = "x"
            player_col += 1
            if player_col == cols:
                player_col = 0
            if matrix[player_rol][player_col] == "D":
                decorations += 1
                items -= 1
            elif matrix[player_rol][player_col] == "G":
                gifts += 1
                items -= 1
            elif matrix[player_rol][player_col] == "C":
                cookies += 1
                items -= 1
            matrix[player_rol][player_col] = "Y"

            step -= 1

    elif command[0] == "left":
        step = int(command[1])
        while True:
            if items == 0:
                condition = True
                break
            if step == 0:
                break
            matrix[player_rol][player_col] = "x"
            player_col -= 1
            if player_col < 0:
                player_col = cols - 1
            if matrix[player_rol][player_col] == "D":
                decorations += 1
                items -= 1
            elif matrix[player_rol][player_col] == "G":
                gifts += 1
                items -= 1
            elif matrix[player_rol][player_col] == "C":
                cookies += 1
                items -= 1
            matrix[player_rol][player_col] = "Y"
            step -= 1

    elif command[0] == "down":
        step = int(command[1])
        while True:
            if items == 0:
                condition = True
                break
            if step == 0:
                break
            matrix[player_rol][player_col] = "x"
            player_rol += 1
            if player_rol == rows:
                player_rol = 0
            if matrix[player_rol][player_col] == "D":
                decorations += 1
                items -= 1
            elif matrix[player_rol][player_col] == "G":
                gifts += 1
                items -= 1
            elif matrix[player_rol][player_col] == "C":
                cookies += 1
                items -= 1
            matrix[player_rol][player_col] = "Y"
            step -= 1

    elif command[0] == "up":
        step = int(command[1])
        while True:
            if items == 0:
                condition = True
                break
            if step == 0:
                break
            matrix[player_rol][player_col] = "x"
            player_rol -= 1
            if player_rol < 0:
                player_rol = rows - 1
            if matrix[player_rol][player_col] == "D":
                decorations += 1
                items -= 1
            elif matrix[player_rol][player_col] == "G":
                gifts += 1
                items -= 1
            elif matrix[player_rol][player_col] == "C":
                cookies += 1
                items -= 1
            matrix[player_rol][player_col] = "Y"
            step -= 1
    if condition:
        break
    command = input().split("-")

if items == 0:
    print("Merry Christmas!")
print("You've collected:")
print(f"- {decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

for z in matrix:
    print(*z, sep=" ")
