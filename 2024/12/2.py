class Region:
    
    def __init__(self, crds, plant):
        pass
    
input = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

input = input.split("\n")
for i in range(len(input)):
    last_plant = ""
    for j in range(len(input[0])):
        if input[i][j] != last_plant:
            input[i].insert(".", j)
        print(input[i][j])        
        
