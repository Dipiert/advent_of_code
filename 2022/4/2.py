import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()


def _ranges_overlap(first, second):
    return any(n for n in first if n in second) or any(n for n in second if n in first)


overlap = 0
for line in inp:
    first_range, second_range = line.split(',')
    first_range = range(int(first_range.split('-')[0]), int(first_range.split('-')[1]) + 1)
    second_range = range(int(second_range.split('-')[0]), int(second_range.split('-')[1]) + 1)
    if _ranges_overlap(first_range, second_range):
        overlap += 1
print(overlap)