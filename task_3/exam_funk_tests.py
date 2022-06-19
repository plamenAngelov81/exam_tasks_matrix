from collections import deque


nice_or_bad_kids = {"Nice": [], "Naughty": [], "Not found": []}
kids_data = [(15, "Ani"), (6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank")]
command_list = ["6-Nice", "5-Naughty", "4-Nice", "3-Naughty", "2-Nice", "1-Naughty"]
command_numbers = []
for i in command_list:
    number = int(i.split("-")[0])
    command_numbers.append(number)

command_queue = deque(command_list)

while command_queue:
    command = command_queue.popleft()
    number = int(command.split("-")[0])
    statement = command.split("-")[1]
    counter = 0
    for kid in range(len(kids_data)):
        current_num = kids_data[kid][0]
        current_kid = kids_data[kid][1]
        if number == current_num:
            counter += 1
    if counter > 1:
        continue

    if counter == 1:
        for i in range(len(kids_data)):
            num = kids_data[i][0]
            if num == number:
                nice_or_bad_kids[statement].append(kids_data[i][1])
                del kids_data[i]
                break

