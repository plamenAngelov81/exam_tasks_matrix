from collections import deque

# take the first firework element
firework_effects = deque(map(int, input().split(", ")))

# take the last boom element
boom_power = list(map(int, input().split(", ")))

palm = 0
willow = 0
cross_fire = 0
result = 0
condition = False

while firework_effects and boom_power:
    current_firework = firework_effects[0]
    current_power = boom_power[-1]
    result = current_power + current_firework
    if current_power > 0 and current_firework > 0:
        if result % 3 == 0 and result % 5 != 0:
            palm += 1
            firework_effects.popleft()
            boom_power.pop()
        elif result % 3 != 0 and result % 5 == 0:
            willow += 1
            firework_effects.popleft()
            boom_power.pop()
        elif result % 3 == 0 and result % 5 == 0:
            cross_fire += 1
            firework_effects.popleft()
            boom_power.pop()
        else:
            firework_effects[0] -= 1
            moved_firework = firework_effects.popleft()
            firework_effects.append(moved_firework)
    else:
        if current_firework <= 0 and current_power <= 0:
            firework_effects.popleft()
            boom_power.pop()
        elif current_firework <= 0:
            firework_effects.popleft()
        elif current_power <= 0:
            boom_power.pop()

    if palm >= 3 and willow >= 3 and cross_fire >= 3:
        condition = True
        break

if condition:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if boom_power:
    print(f" Explosive Power left: {', '.join(map(str, boom_power))}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {cross_fire}")
