import os
import re
with open(os.path.join(os.path.dirname(__file__), 'sample.txt')) as f:
    inp = f.read().splitlines()

def find():
    


filesizes = {}
for cmd in inp:
    if '$' not in cmd:
        cmd = cmd.split()
        if cmd[0].isnumeric():
            filesizes[cmd[1]] = cmd[0]
print(filesizes)

for file in filesizes:
    find(file)