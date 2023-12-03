import os
import re
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()


def remove_borders(i, j, rows):
    new_rows = []
    for i, row in enumerate(rows):
        new_row = []
        for j, item in enumerate(row):
            if i == 0 or i == len(rows[0])-1 or j == 0 or j == len(rows)-1:
                continue
            else:
                new_row.append(rows[i][j])
        if new_row:
            new_rows.append(new_row)
    return new_rows


rows = []

for line in inp:
    line = list(line)
    row = []
    for item in line:
        row.append(int(item))
    rows.append(row)
print(rows)

dim = len(rows)
visible = 0


def path_to_border_h(rows, i, j):
    return rows[i][:j], rows[i][j+1:], item


def path_to_border_v(rows, i, j):
    item = rows[i][j]
    if i == 0 or i == len(rows) - 1:
        return [], [], item
    else:
        col = [row[j] for row in rows]
        return col[:i], col[i+1:], item


def look_around(rows, i, j):
    item = rows[i][j]
    left = rows[i][:j]
    right = rows[i][j + 1:]
    col = [row[j] for row in rows]
    top = col[:i]
    bottom = col[i+1:]
    return top, left, right, bottom, item


def how_many(direction, item):
    if direction == [0, 5]:
        print()
    visibility = 0
    for tree in direction:
        if tree < item:
            visibility += 1
        if tree >= item:
            visibility += 1
            break
    return visibility

visibility = 0
max_visibility = 0
for i, row in enumerate(rows):
    for j, item in enumerate(row):
        top, left, right, bottom, item = look_around(rows, i, j)
        if not top or not left or not right or not bottom:
            #print(f'top: {top} left: {left} right: {right} bottom: {bottom}')
            continue
        #print(f'top: {top} left: {left} right: {right} bottom: {bottom}')

        v_top = how_many(reversed(top), item)
        #print(f'There is: {v_top} to the top of {item}')

        v_left = how_many(reversed(left), item)
        #print(f'There is: {v_left} to the left of {item}')

        v_right = how_many(right, item)
        #print(f'There is: {v_right} to the right of {item}')

        v_bottom = how_many(bottom, item)
        #print(f'There is: {v_bottom} to the bottom of {item}')

        visibility = v_top * v_left * v_right * v_bottom
        max_visibility = max(max_visibility, visibility)
        #print(f'Max Visibility: {max_visibility}')

# 1861200 too high
410400

print(max_visibility)
