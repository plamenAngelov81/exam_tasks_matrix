def start_spring(**objects):
    result = ""
    type_dict = {}
    for i in objects:
        item = i
        value = objects[i]
        if value not in type_dict:
            type_dict[value] = []
        type_dict[value].append(item)

    sorted_list = sorted(type_dict.items(), key=lambda x: (-len(x[1]), x[0], x[1]))
    for i in sorted_list:
        list_of_objects = i[1]
        sorted_list_of_objects = sorted(list_of_objects)
        result += f"{i[0]}:\n"
        for obj in sorted_list_of_objects:
            result += f"-{obj}\n"
    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))
