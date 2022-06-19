import re


def is_inside(x, y, num):
    return 0 <= x < num and 0 <= y < num


players = input().split(", ")
regex = r"\d+"
matrix = []
player_stat = [[players[0], 501], [players[1], 501]]
size = 7

for _ in range(size):
    row = input().split()
    matrix.append(row)

turns = 1
counter = 0
coordinates = input()
while True:
    reg_result = re.finditer(regex, coordinates)
    player_coordinates = []
    for i in reg_result:
        player_coordinates.append(int(i.group()))
    player_row, player_col = player_coordinates

    if not is_inside(player_row, player_col, size):
        counter += 1
        player_switch = player_stat[0]
        player_stat.pop(0)
        player_stat.append(player_switch)
        coordinates = input()
        if counter % 2 == 0:
            turns += 1
        continue

    if matrix[player_row][player_col] == "B":
        print(f"{player_stat[0][0]} won the game with {turns} throws!")
        break
    elif matrix[player_row][player_col] == "D":
        current_points = (int(matrix[0][player_col]) + int(matrix[size - 1][player_col]) + int(matrix[player_row][0])
                          + int(matrix[player_row][size - 1])) * 2
        player_stat[0][1] -= current_points
        if player_stat[0][1] <= 0:
            print(f"{player_stat[0][0]} won the game with {turns} throws!")
            break
    elif matrix[player_row][player_col] == "T":
        current_points = (int(matrix[0][player_col]) + int(matrix[size - 1][player_col]) + int(matrix[player_row][0])
                          + int(matrix[player_row][size - 1])) * 3
        player_stat[0][1] -= current_points
        if player_stat[0][1] <= 0:
            print(f"{player_stat[0][0]} won the game with {turns} throws!")
            break
    else:
        player_stat[0][1] -= int(matrix[player_row][player_col])
        if player_stat[0][1] <= 0:
            print(f"{player_stat[0][0]} won the game with {turns} throws!")
            break

    current_player = player_stat[0]
    player_stat.pop(0)
    player_stat.append(current_player)
    counter += 1
    if counter % 2 == 0:
        turns += 1
    coordinates = input()
