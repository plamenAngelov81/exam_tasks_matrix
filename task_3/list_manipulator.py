
def list_manipulator(*args):
    base_list = args[0]
    first_command = args[1]
    second_command = args[2]

    if first_command == "add":
        add_numbers = args[3:]
        if second_command == "beginning":
            for i in range(len(add_numbers) - 1, -1, - 1):
                base_list.insert(0, add_numbers[i])
        elif second_command == "end":
            for j in range(len(add_numbers)):
                base_list.append(add_numbers[j])

    elif first_command == "remove":
        if second_command == "end":
            if len(args) == 3:
                base_list.pop()
            if len(args) > 3:
                step = args[3]
                for i in range(step):
                    base_list.pop()
        elif second_command == "beginning":
            if len(args) == 3:
                element = base_list[0]
                base_list.remove(element)
            if len(args) > 3:
                step = args[3]
                for i in range(step):
                    element = base_list[0]
                    base_list.remove(element)

    return base_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
