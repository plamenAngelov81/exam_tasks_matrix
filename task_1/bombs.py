from collections import deque

# take first effect
effects = deque(int(x) for x in input().split(", "))

# take last casing
casings = [int(y) for y in input().split(", ")]

cherry_bomb = 0
datura_bomb = 0
smoke_decoy_bomb = 0
bomb_pouch = False

while effects and casings:
    effect = effects[0]
    casing = casings[-1]
    result = effect + casing

    if result == 40:
        datura_bomb += 1
        effects.popleft()
        casings.pop()
    elif result == 60:
        cherry_bomb += 1
        effects.popleft()
        casings.pop()
    elif result == 120:
        smoke_decoy_bomb += 1
        effects.popleft()
        casings.pop()
    else:
        casings[-1] -= 5

    if cherry_bomb >= 3 and datura_bomb >= 3 and smoke_decoy_bomb >= 3:
        bomb_pouch = True
        break

# line 1
if bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

# line 2
if len(effects) == 0:
    print("Bomb Effects: empty")
elif len(effects) > 0:
    print(f"Bomb Effects: {', '.join(map(str, effects))}")

# Line 3
if len(casings) == 0:
    print("Bomb Casings: empty")
elif len(casings) > 0:
    print(f"Bomb Casings: {', '.join(map(str, casings))}")

print(f"Cherry Bombs: {cherry_bomb}")
print(f"Datura Bombs: {datura_bomb}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bomb}")
