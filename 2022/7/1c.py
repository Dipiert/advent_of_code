import os
from pprint import pprint as pp
with open(os.path.join(os.path.dirname(__file__), 'sample.txt')) as f:
    inp = f.read().splitlines()

from collections import defaultdict

sizes = defaultdict(int)
path = []
for cmd in inp:
    cmd = cmd.split()
    if cmd[1] == 'cd':
        if cmd[2] == '..':
            path.pop()
        else:
            path.append(cmd[-1])
    elif cmd[1] == 'ls':
        continue
    else:
        size = 0
        try:
            size = int(cmd[0])
            path.append(cmd[-1])
        except:
            pass
        print(path, size)



# class Tree:
#
#     def __init__(self):
#         self.root = '/'
#         self.nodes = defaultdict(list())
#
#     def add_node(self, file, parent='/'):
#         if file not in self.nodes:
#             self.nodes.append(file)
#
#     def __repr__(self):
#         return f"Tree: {self.nodes}"
#
#
# t = Tree()
# for cmd in inp:
#     if cmd == '$ cd /':
#         continue
#     elif cmd == '$ ls':
#         continue
#     elif cmd.startswith('$ cd '):
#         dir = cmd.split('$ cd ')[1]
#         inside = dir
#         #t.add_node({dir:0})
#     elif cmd.startswith('dir '): # a directory
#         dir = cmd.split('dir ')[1]
#         t.add_node({dir: 0})
#     else: # a file
#         size = cmd.split()[0]
#         file = cmd.split()[1]
#         t.add_node([{file: size}])
#
# print(t)
# def get_dirs(inp):
#     dirs = []
#     for line in inp:
#         if line.startswith('dir '):
#             dirs.append(line.split('dir ')[1])
#     return dirs
#
#
# def calc_dir_size(dir, inp, total=0):
#     print(f'Calculating size of {dir}')
#     found = False
#     for cmd in inp:
#         if not found:
#             if cmd == f'$ cd {dir}':
#                 total = 0
#                 found = True
#                 continue
#         else:
#             if cmd == '$ ls':
#                 continue
#             elif cmd.startswith('$ cd '):
#                 found = False
#             else:
#                 if cmd.startswith('dir '):
#                     calc_dir_size(cmd.split('dir ')[1], inp, total)
#                 else:
#                     total += int(cmd.split(' ')[0])
#                     print(f'Total of {dir} is {total}')
#
#
# dirs = get_dirs(inp)
# for dir in dirs:
#     calc_dir_size(dir, inp)
#
# # ls = False
# # levels = []
# # #inp = inp)
# # for cmd in inp:
# #     if not ls:
# #         if cmd.startswith('$ ls'):
# #             ls = True
# #             level = []
# #             continue
# #     else:
# #         if not cmd.startswith('$ '):
# #             level.append(cmd)
# #         else:
# #             ls = False
# #             levels.append(level)
# # pp(levels)
