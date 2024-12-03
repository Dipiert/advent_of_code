from pathlib import Path
import re

do = True

def get_file_as_str(path='input.txt'):
    p = Path(__file__).with_name(path)

    with p.open("r") as f:
        file = f.read()
        
    return file

def mul(a, b):    
    if do:
        print(f"Doing {a} * {b}")
        return a * b
    
def _do():
    global do
    do = True
    
def dont():
    global do
    do = False

#input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
#input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
input = get_file_as_str()
tot = 0
for c in input:
    pts = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", input)
for m in pts:
    print(m)
    if m.startswith("don't"):
        dont()
    elif m.startswith("do"):
        _do()
    else:
        res = eval(m)
        if res is not None:
            tot += eval(m)
print(tot)