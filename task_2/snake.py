size = int(input())

territory = []
current_row = 0
current_col = 0
snake_hole = []

for n in range(size):
    territory.append(list(input()))

for i in range(size):
    for j in range(size):
        if territory[i][j] == "S":
            current_row = i
            current_col = j
        elif territory[i][j] == "B":
            snake_hole.append([i, j])

food = 0
command = input()
while True:

    territory[current_row][current_col] = "."
    if command == "up":
        current_row -= 1
    if command == "down":
        current_row += 1
    if command == "left":
        current_col -= 1
    if command == "right":
        current_col += 1

    if 0 <= current_row < size and 0 <= current_col < size:

        if territory[current_row][current_col] == "*":
            food += 1
            territory[current_row][current_col] = "S"
        elif territory[current_row][current_col] == "B":
            territory[current_row][current_col] = "."
            if current_row == snake_hole[0][0] and current_col == snake_hole[0][1]:
                current_row = snake_hole[1][0]
                current_col = snake_hole[1][1]
                territory[current_row][current_col] = "S"
            elif current_row == snake_hole[1][0] and current_col == snake_hole[1][1]:
                current_row = snake_hole[0][0]
                current_col = snake_hole[0][1]
                territory[current_row][current_col] = "S"
    else:
        print("Game over!")
        print(f"Food eaten: {food}")
        for x in territory:
            print(f"{''.join(x)}")
        break

    if food == 10:
        break

    command = input()

if food == 10:
    print("You won! You fed the snake.")
    print(f"Food eaten: {food}")
    for y in territory:
        print(f"{''.join(y)}")
