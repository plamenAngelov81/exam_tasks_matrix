def numbers_searching(*args):
    result = []
    counted_nums = set()
    for i in args:
        if args.count(i) > 1:
            counted_nums.add(i)

    unique_number_set = set(args)

    list_counted_numbers = []
    for i in counted_nums:
        list_counted_numbers.append(i)

    list_counted_numbers.sort()

    unique_number_list = sorted([x for x in unique_number_set])

    for i in range(unique_number_list[0], unique_number_list[-1]):
        if i not in unique_number_list:
            result.append(i)

    result.append(list_counted_numbers)
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))

