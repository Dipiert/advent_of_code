import os

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()


def _move_h(dir, h):
    if dir == 'R':
        h = h[0] + 1, h[1]
        print(f'Moved H to R. Pos: ({h[0]},{h[1]})')
    elif dir == 'U':
        h = h[0], h[1] + 1
        print(f'Moved H to U. Pos: ({h[0]},{h[1]})')
    elif dir == 'L':
        h = h[0] - 1, h[1]
        print(f'Moved H to L. Pos: ({h[0]},{h[1]})')
    elif dir == 'D':
        h = h[0], h[1] - 1
        print(f'Moved H to D. Pos: ({h[0]},{h[1]})')
    return h


t = 0, 0
h = 0, 0
t_steps = set()
t_steps.add((0, 0))
for line in inp:
    dir, steps = line.split(' ')
    steps = int(steps)
    print(dir, steps)
    while steps:
        steps -= 1
        h = _move_h(dir, h)

        if abs(t[0] - h[0]) == 2:  # away in x
            if t[1] == h[1]:  # same y
                if t[0] < h[0]:
                    t = t[0] + 1, t[1]  # move t right
                    print(f'Moved T to R. Pos: ({t[0]},{t[1]})')
                    t_steps.add(t)
                else:
                    t = t[0] - 1, t[1]  # move t left
                    print(f'Moved T to L. Pos: ({t[0]},{t[1]})')
                    t_steps.add(t)
            elif abs(t[1] - h[1]) == 1:  # away and x AND Y, move oblicuous
                if t[1] < h[1]:
                    t = t[0], t[1]+1
                    if t[0] < h[0]:
                        t = t[0]+1, t[1]
                        print(f'Moved T to UR. Pos: ({t[0]},{t[1]})')
                        t_steps.add(t)
                    else:
                        t = t[0]-1, t[1]
                        print(f'Moved T to UL. Pos: ({t[0]},{t[1]})')
                        t_steps.add(t)
                else:
                    t = t[0], t[1]-1
                    if t[0] < h[0]:
                        t = t[0]+1, t[1]
                        print(f'Moved T to UR. Pos: ({t[0]},{t[1]})')
                        t_steps.add(t)
                    else:
                        t = t[0]-1, t[1]
                        print(f'Moved T to DL. Pos: ({t[0]},{t[1]})')
                        t_steps.add(t)

        elif abs(t[1] - h[1]) == 2:  # away in y
            if t[0] == h[0]:  # same x
                if t[1] < h[1]:
                    t = t[0], t[1] + 1  # move up
                    print(f'Moved T to U. Pos: ({t[0]},{t[1]})')
                    t_steps.add(t)
                else:
                    t = t[0], t[1] - 1 # move down
                    print(f'Moved T to D. Pos: ({t[0]},{t[1]})')
                    t_steps.add(t)
            elif abs(t[0] - h[0]) == 1:
                if t[0] < h[0]:
                    t = t[0]+1, t[1]
                    if t[1] < h[1]:
                        t = t[0], t[1] + 1
                        print(f'Moved T to RU. Pos: ({t[0]},{t[1]})')
                        t_steps.add(t)
                    else:
                        t = t[0], t[1] - 1
                        print(f'Moved T to RD. Pos: ({t[0]},{t[1]})')
                        t_steps.add(t)
                else:
                    t = t[0] - 1, t[1]
                    if t[1] < h[1]:
                        t = t[0], t[1]+1
                        print(f'Moved T to UL. Pos: ({t[0]},{t[1]})')
                        t_steps.add(t)
                    else:
                        t = t[0], t[1]-1
                        print(f'Moved T to DL. Pos: ({t[0]},{t[1]})')
                        t_steps.add(t)

print(t_steps)
print(len(t_steps))
