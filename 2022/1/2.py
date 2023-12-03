import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()

max_calories = [0, 0, 0]
calories_by_elf = 0

for food in inp:
    if food == '':
        if calories_by_elf > max_calories[0]:
            if max_calories[0] > max_calories[1]:
                max_calories[1] = max_calories[0]
            elif max_calories[0] > max_calories[2]:
                max_calories[2] = max_calories[0]
            max_calories[0] = calories_by_elf

        elif calories_by_elf > max_calories[1]:

            if max_calories[1] > max_calories[0]:
                max_calories[0] = max_calories[1]
            elif max_calories[1] > max_calories[2]:
                max_calories[2] = max_calories[1]
            max_calories[1] = calories_by_elf

        elif calories_by_elf > max_calories[2]:
            if max_calories[2] > max_calories[0]:
                max_calories[0] = max_calories[2]
            elif max_calories[2] > max_calories[1]:
                max_calories[1] = max_calories[2]
            max_calories[2] = calories_by_elf

        calories_by_elf = 0
    else:
        calories_by_elf += int(food)

print(max_calories)
print(sum(max_calories))
#200562 is too low