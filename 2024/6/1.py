#incomplete 
from itertools import cycle
from pathlib import Path

GUARD = '^'

input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def get_file_as_str(path='input.txt'):
    p = Path(__file__).with_name(path)

    with p.open("r") as f:
        file = f.read()
        
    return file

input = get_file_as_str()

def guard_pos(input):
    for i, l in enumerate(input.splitlines()):
        if GUARD in l:
            return i, l.index(GUARD)
        
def trace(starting_point, obstacle, input, direction):
    """
    Returns a new starting point after tracing the path
    """
    if direction == 'up':
        for i in range(obstacle[0]+1, starting_point[0]): # skip the obstacle itself
            input[i] = "".join([
                input[i][:starting_point[1]],
                "X",
                input[i][starting_point[1]+1:]
            ])
        return (obstacle[0]+1, obstacle[1]+1)
    
    if direction == "right":
        row = input[starting_point[0]] 
        input[starting_point[0]] = "".join([
            row[:row.index("X")],
            "X" * (obstacle[1] - starting_point[1] + 1),
            row[row.index("X") + 1 + (obstacle[1] - starting_point[1]):]
        ])
        return (starting_point[0], row.index("X") + (obstacle[1] - starting_point[1]))
    
    if direction == "down":
        for i in range(starting_point[0]+1, obstacle[0]):
            row = input[i]
            input[i] = "".join([
                row[:obstacle[1]],
                "X",
                row[obstacle[1]+1:]
            ]
            )
        return (obstacle[0]-1, obstacle[1])
    
    if direction == "left":
        row = input[starting_point[0]]
        input[starting_point[0]] = "".join([
            row[:obstacle[1]],
            "#",
            "X" * (starting_point[1] - obstacle[1]),
            row[len(row[:obstacle[1]]) + 1 + (starting_point[1] - obstacle[1]):]
        ])
        return (
            starting_point[0],
            input[starting_point[0]].index("X"),
        )
        
def search_obstacle(starting_point, input, direction):
    if direction == "up":
        for i in range(starting_point[0]-1, -1, -1):
            if input[i][starting_point[1]] == '#':#or i == 0:
                return (i, starting_point[1])
            if i == 0:
                return (i, starting_point[1], "stop")
    
    if direction == 'right':
        row = input[starting_point[0]][starting_point[1]:] # skip the obstacle
        x = starting_point[0]
        if "#" in row:
            y = row.index("#") + starting_point[1]
            return (x, y)
        else:
            y = len(row)
            z = "stop"
        return (x, y, z)

    if direction == "down":
        for i in range(starting_point[0]+1, len(input)):
            if input[i][starting_point[1]] == '#':
                return (i, starting_point[1])
        return (len(input), starting_point[1], "stop")
            
    if direction == "left":
        row = input[starting_point[0]]
        if "#" in row:
            return (starting_point[0], row.index("#"))
        else:
            return (starting_point[0], row.index("#"), "stop")

            
def walk(starting_point, input):
    directions = cycle(["up", "right", "down", "left"])
    for direction in directions:
        obstacle = search_obstacle(starting_point, input, direction)
        print(f"Tracing {direction} from {starting_point}. Obstacle at {obstacle}")
        starting_point = trace(starting_point, obstacle, input, direction)
        if len(obstacle) == 3:
            break
    tot = 0
    for r in input:
        tot += r.count("X")
    print("\n".join(input))
    print(tot)
    
            
if __name__ == '__main__':
    gpos = guard_pos(input)
    input = input.split("\n")
    walk(gpos, input)