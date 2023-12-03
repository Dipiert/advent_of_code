import os


def _calc_priority(item):
    if item.islower():
        return ord(item) - 96
    return ord(item) - 38


priorities_sum = 0
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()

groups = [inp[i:i+3] for i in range(0, len(inp), 3)]
for group in groups:
    rucksack1, rucksack2, rucksack3 = group[0], group[1], group[2]
    for item in rucksack1:
        if item in rucksack2 and item in rucksack3:
            badge = item
            priorities_sum += _calc_priority(badge)
            break

print(priorities_sum)


