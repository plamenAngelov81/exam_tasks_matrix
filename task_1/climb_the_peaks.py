from collections import deque

daily_portions = list(map(int, input().split(", ")))
daily_stamina = deque(map(int, input().split(", ")))

mission_completed = False

peak_difficulty = {
    'Vihren': 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70,
}

peaks = [
    'Vihren',
    'Kutelo',
    'Banski Suhodol',
    'Polezhan',
    'Kamenitza'
]

conquered_peaks = []


def get_current_stamina(current_food, current_stamina):
    return current_food + current_stamina


def get_conquered_peaks(peak_list):
    some_result = ''
    for peak in peak_list:
        some_result += f'{peak}\n'
    return some_result


while daily_portions and daily_stamina:
    food = daily_portions.pop()
    stamina = daily_stamina.popleft()

    result = get_current_stamina(food, stamina)
    current_peak = peaks[0]
    if result >= peak_difficulty[current_peak]:
        conquered_peaks.append(current_peak)
        peaks.pop(0)
        if not peaks:
            mission_completed = True
            break

if mission_completed:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print('Conquered peaks:')
    print(get_conquered_peaks(conquered_peaks))
