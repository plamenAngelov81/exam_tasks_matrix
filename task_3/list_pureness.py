def best_list_pureness(*args):
    ll = args[0]
    step = 0
    rotations = 0
    result = 0

    while True:
        if len(ll) == 0:
            break

        current_result = 0
        for j in range(len(ll)):
            index_number_multy = j * ll[j]
            current_result += index_number_multy

        if current_result > result:
            result = current_result
            rotations = step
        element = ll[-1]
        ll.pop()
        ll.insert(0, element)
        if step == args[1]:
            break
        step += 1
    return f"Best pureness {result} after {rotations} rotations"


test = ([], 4)
result = best_list_pureness(*test)
print(result)
