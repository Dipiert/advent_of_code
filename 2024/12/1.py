from collections import defaultdict

area_by_plant = defaultdict(int)
perimeter_by_plant = defaultdict(int)

# input = """AAAA
# BBCD
# BBCC
# EEEC
# """

input = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

def transpose(input):
    t = []
    
    for i in range(len(input)):
        row = []
        for j in range(len(input[0])):
            row.append(input[j][i])
        t.append(row)
    
    return t

def calc_area(i, j, input, t):
    print(f"Horizontal: {input[i][j]}. Area: {input[i].count(input[i][j])}")
    print(f"Vertical: {input[i][j]}. Area: {t[j].count(input[i][j])}")
    print()
    return input[i].count(input[i][j])

def how_many_around(plant, input, i, j):
    qty = 0
    if j == 0 or plant != input[i][j-1]:
        qty += 1
    if j == len(input)-1 or plant != input[i][j+1]:
        qty += 1
    if i == 0 or plant != input[i-1][j]:
        qty +=1
    if i == len(input[0])-1 or plant != input[i+1][j]:
        qty += 1

    print(f"Plant {plant} at {(i, j)} has per {qty}")
    return qty
                    
def calc_area_perimeter(input):
    for i in range(len(input)):
        last_plant = ""
        for j in range(len(input[0])):
            while input[i][j] != last_plant:
                last_plant = input[i][j]            
                area = calc_area(i, j, input, t)
                area_by_plant[last_plant] += area
                
    
    for i in range(len(input)):
        for j in range(len(input[0])):
            #while input[i][j] != last_plant:
            #per = 0
            last_plant = input[i][j] 
            #per = how_many_around(last_plant, input, i, j)
            perimeter_by_plant[last_plant] += how_many_around(last_plant, input, i, j)
            
        #area_perimeter_by_plant[last_plant] += per
    
                
    print(area_by_plant)
    print("*" * 10)
    print(perimeter_by_plant)
    
plant_regions = {}

def regions(input, plants):
    from pprint import pprint
    for p in plants:
        view = []
        for i in range(len(input)):
            row = []
            for j in range(len(input[0])):                
                if input[i][j] != p:
                    row.append(".")
                else:
                    row.append(p)
            view.append(row)
                    #input_view = input[i][:j] + '.' + input[i][j+1:]
                    #input_view[i][j] = '.'
        #plant_regions[p] = input_view
        pprint(view)
        print()

    # for each plant, delete everything which is not it.

if __name__ == '__main__':
    plants = set(input) #- '\n'
    plants.remove('\n')
    input = input.splitlines()
    #t = transpose(input)
    regions(input, plants)
    #calc_area_perimeter(input)