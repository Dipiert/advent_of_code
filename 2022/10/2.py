import os

with open(os.path.join(os.path.dirname(__file__), 'sample.txt')) as f:
    inp = f.read().splitlines()

x = 1
cycle = 1
lineno = -1
add_started = False
track_x = {}
print(len(inp))
total_strength = 0
while cycle <= 220:
    track_x[cycle] = x
    if not add_started:
        lineno += 1
    line = inp[lineno]

    #print(f'While starting cycle {cycle}, x is {x}')
    if line == 'noop':
        cycle += 1
    else:
        inst, value = line.split(' ')
        value = int(value)
        add_started = not add_started
        if not add_started:
            x += persisted
        persisted = value
        cycle += 1

cycle = 0
while cycle <= 220:
    for x in track_x:
        sprite_pos = '###' + '.' * 37
        print(sprite_pos)





