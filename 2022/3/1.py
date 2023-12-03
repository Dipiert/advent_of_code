import os


def _calc_priority(item):
    if dupe.islower():
        return ord(dupe) - 96
    return ord(dupe) - 38


priorities_sum = 0
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()
for line in inp:
    dupes = []
    first_half, second_half = set(line[0:len(line)//2]), set(line[len(line)//2:])

    for item in first_half:
        if item in second_half:
            dupes.append(item)

    for dupe in dupes:
        priorities_sum += _calc_priority(item)

print(priorities_sum)
