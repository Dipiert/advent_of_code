import os

flatten_nodes = set()


class Node:

    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.size = 0

    def __repr__(self):
        return f'{self.name} - Children: {self.children}'

    def find(self, name):
        if self.name == name:
            return self
        for node in self.children:
            if node.find(name):
                return node

root = Node('/')
flatten_nodes.add(root)

# def find_node(node, name):
#     if name == 'd':
#         print()
#     if name == node.name:
#         return node
#     for c in node.children:
#         if c.name == name:
#             return c
#         else:
#             return find_node(c, name)


with open(os.path.join(os.path.dirname(__file__), 'sample.txt')) as f:
    inp = f.read().splitlines()


for cmd in inp:
    parts = cmd.split()
    if parts[0] == '$':
        if parts[1] == 'cd':
            if parts[2] == '/':
                cwd = root
            else:
                dir_name = parts[2]
                if dir_name == '..':
                    print(f'cd ..')
                    cwd = cwd.parents[0]
                else:
                    node = cwd.find(dir_name)
                    cwd = node #.index(dir_name)
                #print(f'Moving to: {cwd}')
                print(f'Just moved to: {cwd}')
        elif parts[1] == 'ls':
            pass
    else:
        if parts[0] == 'dir':
            n = Node(parts[1])
            n.parents.append(cwd)
            cwd.children.append(n)
            flatten_nodes.add(n)
            print(f'cwd: {cwd}')
        else:
            cwd.size += int(parts[0])
            print(f'{cwd.name} total size: {cwd.size} - Just added {parts[1]} ({int(parts[0])})')
            for c in cwd.parents:
                c.size += int(parts[0])
                print(f'Propagating size. Total: {cwd.name}: {cwd.size} - Just added {parts[1]} ({int(parts[0])}) to {c.name}')


def print_sizes(node, printed=[]):
    print(f'{node}: {root.size}')
    for c in node.children:
        return print_sizes(c)

#print(flatten_nodes)
#print_sizes(root, [])
print("*" * 80)
total = 0
for i in flatten_nodes:
    print(i, i.size)
    if i.size <= 100000:
        total += i.size
print(total)
# def prune(n, to_consider=[]):
#     for c in n.children:
#         print(f'CHECKING {c} AS {n} CHILDREN')
#         if c.size >= 100000:
#             prune(c, to_consider)
#         else:
#             print(f'WILL CONSIDER {c} WITH SIZE {c.size}')
#             to_consider.append(c)
#
# to_discard = []
# prune(root, to_discard)
# total = 0
# for n in to_discard:
#     total += n.size
# print(total)

# 1558952 too high

