import os


crates_positions = (1, 5, 9, 13, 17, 21, 25, 29, 33)


def make_stacks(inp):
    stacks = [[], [], [], [], [], [], [], [], []]
    for line in inp:
        if '[' in line:
            for crate_position in crates_positions:
                try:
                    if line[crate_position] != ' ':
                        stack_index = crates_positions.index(crate_position)
                        stacks[stack_index].append(line[crate_position])
                except IndexError:
                    pass
    return stacks
    #print(stacks)


def parse_instructions(inp):
    import re
    instructions = []
    pattern = 'move (.+) from (.+) to (.+)'
    for line in inp:
        if 'move' in line:
            mo = re.match(pattern, line)
            instructions.append(mo.groups())
            #re.split(line)
            #line.split('move')
    #print(instructions)
    return instructions


def run(instructions, stacks):
    for ins in instructions:
        count = int(ins[0])
        _from = int(ins[1]) - 1
        to = int(ins[2]) - 1
        if count > 1:
            #for i in stacks[_from][:count]:
            stacks[to] = stacks[_from][:count] + stacks[to]
            for i in stacks[_from][:count]:
                stacks[_from].remove(i)

        else:
            stacks[_from].reverse()
            stacks[to].insert(0, stacks[_from].pop())
            stacks[_from].reverse()
            from pprint import pprint as pp; pp(stacks)


with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()

stacks = make_stacks(inp)
instructions = parse_instructions(inp)
run(instructions, stacks)

print(stacks)
result = ''
for stack in stacks:
    if stack:
        stack.reverse()
        result += stack.pop()
print(result)


