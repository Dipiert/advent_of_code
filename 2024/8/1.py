from collections import defaultdict
from pathlib import Path

def get_file_as_str(path='input.txt'):
    p = Path(__file__).with_name(path)

    with p.open("r") as f:
        file = f.read()
        
    return file

input = """T.........T.........
...T.........T......
.T.........T........
....................
....................
....................
....................
....................
....................
....................
"""
#input = get_file_as_str()
input = input.splitlines()
        
def find_antinodes2(input, distances, antennas):
    antinodes = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            for antenna in antennas:
                for antenna2 in antennas:
                    if i == 3 and j == 9:
                        print()
                    if antenna != antenna2:
                        #d_a1 = abs(distances[i,j][antenna][0])+abs(distances[i,j][antenna][1])
                        #d_a2 = abs(distances[i,j][antenna2][0])+abs(distances[i,j][antenna2][1])
                        #max_d = max(d_a1, d_a2)
                        #if max_d == d_a1 * 2 or max_d == d_a2 * 2:
                        if input[antenna[0]][antenna[1]] == input[antenna2[0]][antenna2[1]]: # same frequency
                            if distances[i,j][antenna][0] == antenna2[0] - antenna[0] and distances[i,j][antenna][1] == antenna2[1] - antenna[1]:
                                antinodes.add((i, j))
    print(len(antinodes))
    print(antinodes)

def find_antinodes(input, distances, antennas):
    antinodes = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            for antenna in antennas:
                for antenna2 in antennas:
                    if antenna != antenna2:
                        d_a1 = abs(distances[i,j][antenna][0])+abs(distances[i,j][antenna][1])
                        d_a2 = abs(distances[i,j][antenna2][0])+abs(distances[i,j][antenna2][1])
                        max_d = max(d_a1, d_a2)
                        if max_d == d_a1 * 2 or max_d == d_a2 * 2:
                            if input[antenna[0]][antenna[1]] == input[antenna2[0]][antenna2[1]]: # same frequency
                                if distances[i,j][antenna][0] == antenna2[0] - antenna[0] and distances[i,j][antenna][1] == antenna2[1] - antenna[1]:
                                        antinodes.add((i, j))
    print(len(antinodes))

def calc_distances(input, antennas_map, antennas):
    """
    distance is a dict with form:
    (point1 x, point1 Y): [ (antenna1 x, antenna1 y): distance between point1 and antenna1 ]
    """
    distance = {}
    for i in range(len(input)):        
        for j in range(len(input[0])):
            distance[(i, j)] = {}
            for antenna in antennas: 
                distance[(i,j)].update([
                    ((antenna[0], antenna[1]), (antenna[0] - i, antenna[1] - j))
                ])
    return distance

def antennas_loc(antennas_map):
    res = []
    for antenna in antennas_map.values():
        for loc in antenna:
            res.append(loc)
    return res
        

def get_antennas_map(input):
    antennas_map = defaultdict(list)
    for i, l in enumerate(input):
        for j, c in enumerate(l):
            if c != '.':
                antennas_map[c].append((i, j))
    return antennas_map

if __name__ == '__main__':    
    antennas_map = get_antennas_map(input)
    antennas = antennas_loc(antennas_map)
    distances = calc_distances(input, antennas_map, antennas)
    find_antinodes2(input, distances, antennas)