import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()

from collections import defaultdict
path = []
paths = []
size = 0
sizes = defaultdict(int)

for cmd in inp:
    parts = cmd.split()
    if parts[0] == '$':
        if parts[1] == 'cd':
            if parts[2] == '..':
                path.pop()
            else:
                path.append(parts[2])
        elif parts[1] == 'ls':
            pass
    else:
        if parts[0] == 'dir':
            pass
        else:
            size = int(parts[0])

            print(f"Adding {parts[1]}({parts[0]}) to size of {path}.")
            for i in range(len(path)):
                sizes['/'.join(path[:i+1])] += size
            #for dir in '/'.join(path).split('/'):
            #    sizes[dir] += size
            #print(sizes)
            #sizes['/'.join(path)] += size
            #print(f"path: {path} - size: {size}")
            #print(f"Added {parts[1]} to size of {path}. Total: {sizes['/'.join(path)]}")

#print(paths)
total = 0
for file, size in sizes.items():
    if size <= 100000:
        total += size
#print(total)

used_space = sizes.get('/')
total = 70_000_000
required = 30_000_000
free = total - used_space
to_free = required - free
#to_free = required - used_space

ordered_sizes = {_dir: size for _dir, size in sorted(sizes.items(), key=lambda item: item[1])}
for _dir, size in ordered_sizes.items():
    if size < to_free:
        continue
    else:
        print(size)
        print(_dir)
        break

