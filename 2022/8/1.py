import os
import re
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()


def visible_from_edge_as_col(i, j, rows, visible):
    item = rows[i][j]
    if j == 0:
        print(f'{item}({i},{j}) is visible from col')
        visible += 1
    return visible


def visible_from_edge_as_row(i, j, rows, visible):
    item = rows[i][j]
    if i == 0:
        print(f'{item}({i},{j}) is visible from row')
        visible += 1
    return visible


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
visible = 0 #dim * 2 + (dim-2) * 2


def path_to_border_h(rows, i, j):
    if i == 2 and j == 0:
        print()
    item = rows[i][j]
    if j == 0 or j == len(rows[0]) - 1:
        return [], [], item
    else:
        return rows[i][:j], rows[i][j+1:], item


def path_to_border_v(rows, i, j):
    item = rows[i][j]
    if i == 0 or i == len(rows) - 1:
        return [], [], item
    else:
        col = [row[j] for row in rows]
        return col[:i], col[i+1:], item

        #for row in rows:
        #    if j != i:
        #        print(row[j])
            #rows[:i][j], rows[i+1:][j], item


for i, row in enumerate(rows):
    for j, item in enumerate(row):
        left, right, item = path_to_border_h(rows, i, j)
        if not left:
            print(f'{item}({i},{j}) is visible as it is horizontal border')
            visible += 1
            continue
        if max(left) < item:
            print(f'{item}({i},{j}) is visible from left')
            visible += 1
        elif max(right) < item:
            print(f'{item}({i},{j}) is visible from right')
            visible += 1
        else:
            top, bottom, item = path_to_border_v(rows, i, j)
            if not top:
                print(f'{item}({i}, {j}) is visible as it is vertical border')
                visible += 1
                continue
            if max(top) < item or max(bottom) < item:
                visible += 1
print(visible)

# import copy
# normalized = []
# taller = 0
# for i, row in enumerate(rows):
#     taller = max(row)
#     normalized_row = []
#     for j, col in enumerate(row):
#         normalized_row.append(rows[i][j] - taller)
#     normalized.append(normalized_row)
# print(normalized)

        #visible_col = visible_from_edge_as_col(i, j, rows, visible_col)
        #visible_row = visible_from_edge_as_row(i, j, rows, visible_row)

#print(new_mat)
print(visible)
#print(visible_row)

# for row in rows:
#     new_row = []
#     for item in row:
#         new_row.append((9 - int(item)))
#     complement.append(new_row)
# print(complement)