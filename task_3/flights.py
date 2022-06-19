def flights(*args):
    data = [x for x in args]
    counter = 0
    travel_dict = {}
    while True:
        destination = data[counter]
        if destination == "Finish":
            break
        passengers = data[counter + 1]
        if destination not in travel_dict:
            travel_dict[destination] = passengers
        else:
            travel_dict[destination] += passengers
        counter += 2
    return travel_dict
