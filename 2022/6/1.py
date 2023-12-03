import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()
    inp = inp[0]

for i in range(len(inp)-4):
    sliding_window = inp[i:i+4]
    if len(sliding_window) == len(set(sliding_window)):
        break
    i += 1
print(i+4)

