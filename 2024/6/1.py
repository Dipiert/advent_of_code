#incomplete 

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

def guard_pos(input):
    for i, l in enumerate(input.splitlines()):
        if GUARD in l:
            return i, l.index(GUARD)
        
def trace(starting_point, obstacle, input, direction):
    """
    Returns a new starting point after tracing the path
    """
    if direction == 'up':
        for i in range(1, starting_point[0]): # skip the obstacle itself
            input[i] = "".join([input[i][:starting_point[1]], "X", input[i][starting_point[1]+1:]])
        return (obstacle[0]+1, obstacle[1]+1)
    
    if direction == "right":
        row = input[starting_point[0]] 
        input[starting_point[0]] = "".join([
            row[:row.index("X")],
            "X" * (obstacle[1] - starting_point[1]),
            row[row.index("X") + 1 + (obstacle[1] - starting_point[1]):]
        ])
        return (starting_point[0], row.index("X") + (obstacle[1] - starting_point[1]))
    
    if direction == "down":
        for j in range(1, starting_point[1]):
            print(input[j])
            #input[j] = "".join(
            #    [input[j][:starting_point[0]], "X", input[j][starting_point[0]+1:]]
            #)
        #print("\n".join(input))
    #if direction == "down":
    #    print()
    #
        
def search_obstacle(starting_point, input, direction):
    if direction == "up":
        for i in range(starting_point[0]-1, -1, -1):
            if input[i][starting_point[1]] == '#' or i == 0:
                return (i, starting_point[1])
    
    if direction == 'right':
        row = input[starting_point[0]+1] # skip the obstacle
        return (starting_point[0]+1, row.index("#") if "#" in row else len(row))

    if direction == "down":
        for i in range(starting_point[0]+1, len(input)):
            if input[i][starting_point[1]] == '#':
                return (i, starting_point[1])
            #print(input[i][starting_point[1]])
            #print(input[i])

            
def walk(starting_point, input):
    direction = "up"
    obstacle = search_obstacle(starting_point, input, direction)
    starting_point = trace(starting_point, obstacle, input, direction)

    direction = "right"
    obstacle = search_obstacle(obstacle, input, direction) 
    starting_point = trace(starting_point, obstacle, input, direction)

    direction = "down"
    obstacle = search_obstacle(starting_point, input, direction)
    starting_point = trace(starting_point, obstacle, input, direction)
            
    #print(visited)

if __name__ == '__main__':
    gpos = guard_pos(input)
    input = input.split("\n")
    walk(gpos, input)