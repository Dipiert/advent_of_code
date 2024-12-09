import itertools 
from pathlib import Path

def get_file_as_str(path='input.txt'):
    p = Path(__file__).with_name(path)

    with p.open("r") as f:
        file = f.read()
        
    return file



# input ="""190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """

input = get_file_as_str()

# input ="""3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """

def product(qty):
    #yield from itertools.product(*["+*"] * qty)
    yield from itertools.product(*["+*|"] * qty)
    
answer = 0
for l in input.splitlines():
    test_value = int(l.split(": ")[0])
    operands = l.split(": ")[1].split(" ")
    operators = list(product(len(operands)-1))    
 
    for line_operators in operators:
        tot = int(operands[0])
        for i, op in enumerate(line_operators):            
            if op == '+':
                tot += int(operands[i+1])
            elif op == '*':
                tot *= int(operands[i+1])
            else:
                tot = int(str(tot) + str(operands[i+1]))
        if test_value == tot:
            answer += test_value
            print(f"Good: {test_value}")
            break
print(answer)   
