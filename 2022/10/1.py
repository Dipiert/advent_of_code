import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()

x = 1
cycle = 1
lineno = -1
add_started = False
print(len(inp))
total_strength = 0
while cycle <= 220:
    if not add_started:
        lineno += 1
    line = inp[lineno]

    print(f'While starting cycle {cycle}, x is {x}')
    if line == 'noop':
        cycle += 1
    else:
        inst, value = line.split(' ')
        value = int(value)
        add_started = not add_started
        if not add_started:
            x += persisted
            persisted = value
        else:
            persisted = value
        cycle += 1
    if cycle in (20, 60, 100, 140, 180, 220):
        print('*' * 20)
        print(f'Signal strength at cycle {cycle}: {x} * {cycle} = {x * cycle}')
        total_strength += x * cycle
        print('*' * 20)
print(total_strength)


