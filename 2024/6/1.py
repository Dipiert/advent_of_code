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
    #visited = input[:]
    if direction == 'up':
        for i in range(1, starting_point[0]): # skip the obstacle itself
            input[i] = "".join([input[i][:starting_point[1]], "X", input[i][starting_point[1]+1:]])
            
    if direction == "right":
        row = input[starting_point[0]+1] 
        input[starting_point[0]+1]  = "".join([row[:starting_point[1]], "X" * (obstacle - starting_point[1]), row[obstacle:]])

        print("\n".join(input))
        
def search_obstacle(starting_point, input, direction):
    if direction == "up":
        for i in range(starting_point[0]-1, -1, -1):
            if input[i][starting_point[1]] == '#' or i == 0:
                return (i, starting_point[1])
    
    if direction == 'right': # THIS IS WRONG
        for j in range(starting_point[1], len(input[0])):
            row = input[j] # skip the obstacle
            return (j, row.index("#") if "#" in row else len(row))
        #if "#" in row:
        ##    end = row.index("#")
        #else:
        #    end = len(row)
        #print(end)
        #print(row)
        #    print(row[j])
            #print(f"Found Obstacle at {obstacle}")
            #trace(starting_point, obstacle, input, direction)
            
def walk(starting_point, input):
    direction = "up"
    obstacle = search_obstacle(starting_point, input, direction)
    print(f"Found Obstacle at {obstacle}")
    trace(starting_point, obstacle, input, direction)
    direction = "right"
    obstacle = search_obstacle(obstacle, input, direction) 
    trace(starting_point, obstacle, input, direction)
    
    
        #if visited[i][starting_point[1]] == '#':
            
    #print(visited)

if __name__ == '__main__':
    gpos = guard_pos(input)
    input = input.split("\n")
    walk(gpos, input)