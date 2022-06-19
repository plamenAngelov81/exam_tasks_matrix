def words_sorting(*args):
    some_dict = {}
    total_sum = 0

    for word in args:
        if word not in some_dict:
            points = 0
            some_dict[word] = 0
            for letter in word:
                points += ord(letter)
            some_dict[word] += points

    for el in some_dict:
        total_sum += some_dict[el]
    result = []
    if total_sum % 2 == 0:
        for i, j in sorted(some_dict.items(), key=lambda x: x[0]):
            result.append(f"{i} - {j}")
    else:
        for i, j in sorted(some_dict.items(), key=lambda x: -x[1]):
            result.append(f"{i} - {j}")

    return '\n'.join(result)
