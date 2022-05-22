from collections import deque

vowels = deque(input().split())

consonants = input().split()

flowers = {"rose": "rose",
           "tulip": "tulip",
           "lotus": "lotus",
           "daffodil": "daffodil"}
condition = False
while vowels and consonants:
    vow = vowels.popleft()
    cons = consonants.pop()
    for flower in flowers:
        flowers[flower] = flowers[flower].replace(vow, "")
        flowers[flower] = flowers[flower].replace(cons, "")
        if flowers[flower] == "":
            print(f"Word found: {flower}")
            condition = True
            break

    if condition:
        break

if not condition:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
