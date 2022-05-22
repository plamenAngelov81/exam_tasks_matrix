from collections import deque

# take last male
male = deque([int(x) for x in input().split()])

# take first female
female = deque([int(y) for y in input().split()])

match_couples = 0

while male and female:
    current_male = male[-1]
    current_female = female[0]

    if current_male <= 0 and current_female <= 0:
        male.pop()
        female.popleft()
    elif current_male <= 0:
        male.pop()
    elif current_female <= 0:
        female.popleft()

    elif current_male % 25 == 0 and current_male != 0:
        for man in range(2):
            male.pop()
    elif current_female % 25 == 0 and current_female != 0:
        for woman in range(2):
            female.popleft()

    elif current_male == current_female:
        match_couples += 1
        male.pop()
        female.popleft()
    elif current_male != current_female:
        male[-1] -= 2
        female.popleft()


print(f"Matches: {match_couples}")

males_left = list(male)
males_left.reverse()
if len(males_left) > 0:
    print(f"Males left: {', '.join(map(str, males_left))}")
else:
    print("Males left: none")

if len(female) > 0:
    print(f"Females left: {', '.join(map(str, female))}")
else:
    print("Females left: none")
