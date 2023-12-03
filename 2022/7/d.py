from collections import defaultdict
import os

with open(os.path.join(os.path.dirname(__file__), 'sample.txt')) as f:
    inp = f.read().splitlines()

sizes = defaultdict(int)
path = []

for line in inp:
    if line.startswith('$ cd'):
        d = line.split()[-1]
        if d == '..':
            path.pop()
        else:
            path.append(d)
    elif line.startswith('$ ls'):
        continue
    else:
        size, _ = line.split()
        if size.isdigit():
            size = int(size)
            for i in range(len(path)):
                sizes['/'.join(path[:i+1])] += size
print(sizes)
# Part 1
ans = 0
for key, value in sizes.items():
    if value <= 100_000:
        ans += value
print(ans)