import os
import re
with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()

ls = False
cwd = []
for cmd in inp:
    if not ls:
        pat = '\\$ cd (.+)'
        m = re.match(pat, cmd)
        if m:
            dir = m.group(0)
            if dir == '/':
                print('In root...')
                break
        elif cmd == '$ ls':
            ls = True
            break
    else:
        ls = False
        pat = 'dir ()'




