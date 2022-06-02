import re


def is_inside(x, y, num):
    return 0 <= x < num and 0 <= y < num


size = 6
regex = r"[\d]+"
matrix = []

wining_points = 0
for _ in range(size):
    matrix.append(list(input().split()))

for i in range(3):

    coordinates = []
    some_string = input()
    result = re.finditer(regex, some_string)
    for j in result:
        coordinates.append(int(j.group()))
    row, col = coordinates
    if not is_inside(row, col, size) or matrix[row][col] != "B":
        continue
    if matrix[row][col] == "B":
        matrix[row][col] = "0"
        down_counter = 1
        while 0 <= row + down_counter < size:
            wining_points += int(matrix[row + down_counter][col])
            down_counter += 1
        up_counter = 1
        while 0 <= row - up_counter < size:
            wining_points += int(matrix[row - up_counter][col])
            up_counter += 1
if wining_points < 100:
    diff = 100 - wining_points
    print(f"Sorry! You need {diff} points more to win a prize.")
elif 100 <= wining_points <= 199:
    print(f"Good job! You scored {wining_points} points, and you've won Football.")
elif 200 <= wining_points <= 299:
    print(f"Good job! You scored {wining_points} points, and you've won Teddy Bear.")
elif wining_points >= 300:
    print(f"Good job! You scored {wining_points} points, and you've won Lego Construction Set.")
