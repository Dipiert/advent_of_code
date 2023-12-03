import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()

max_calories = 0
calories_by_elf = 0

for food in inp:
    if food == '':
        max_calories = max(max_calories, calories_by_elf)
        calories_by_elf = 0
    else:
        calories_by_elf += int(food)

print(max_calories)
