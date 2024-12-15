import re 
from sympy import symbols, Eq, solve

from pathlib import Path

def get_file_as_str(path='input.txt'):
    p = Path(__file__).with_name(path)

    with p.open("r") as f:
        file = f.read()
        
    return file

input = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

input = get_file_as_str()


# input = """Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450
# """

def parse_lines(lines):    
    claws = []
    ax, ay, bx, by, px, py = 0, 0, 0, 0, 0, 0
    for line in lines:        
        m = re.match("Button A: X\+(.*), Y\+(.*)", line)
        if m:
            ax = int(m.group(1))
            ay = int(m.group(2))
        m = re.match("Button B: X\+(.*), Y\+(.*)", line)
        if m:
            bx = int(m.group(1))
            by = int(m.group(2))
        m = re.match("Prize: X=(.*), Y=(.*)", line)
        if m:
            px = int(m.group(1))
            py = int(m.group(2))
        claw = {
            "A": (ax, ay),
            "B": (bx, by),
            "Prize": (px, py)
        }
        if line == "":
            claws.append(claw)
    claws.append(claw)

    return claws

def calc_button_presses(c):
    
    x, y = symbols('x y')
    eq1 = Eq( c["A"][0]*x + c["B"][0]*y, c["Prize"][0] + 10000000000000)
    eq2 = Eq( c["A"][1]*x + c["B"][1]*y, c["Prize"][1] + 10000000000000)
    
    solution = solve((eq1, eq2), (x, y))
    if solution[x] != int(solution[x]) or  solution[y] != int(solution[y]):
        print(f"No solution for {c}")
        return 0
    else:
        cost = solution[x]*3 + solution[y]
        print(f"Solution: {solution}")
        print(f"Cost: {cost}")
        return cost
    
    # x_preferred = ("B", c["B"][0])
    # if c["A"][0] >= c["B"][0]:
    #     x_preferred = ("A", c["A"][0])
        
    # if x_preferred[0] == "A":        
    #     button_presses = c["Prize"][0] // x_preferred[1]
        #while button_presses * x_preferred[1] + c["B"][0] < c["Prize"][0]:
        #    button_presses -= 1
        #print(f"For X, should press A {button_presses} times")
    
        
    #print(f"For {c} in X I prefer: {x_preferred}")
    

if __name__ == '__main__':
    total_cost = 0
    input = input.splitlines()
    claws = parse_lines(input)
    for c in claws:
        total_cost += calc_button_presses(c)
    print(total_cost)
