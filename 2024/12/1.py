from collections import defaultdict

area_perimeter_by_plant = defaultdict(int)

input = """AAAA
BBCD
BBCC
EEEC
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
    if input[i][j] == 'C':
        print()
    print(f"Horizontal: {input[i][j]}. Area: {input[i].count(input[i][j])}")
    print(f"Vertical: {input[i][j]}. Area: {t[j].count(input[i][j])}")
    print()
    return input[i].count(input[i][j])

def how_many_around(plant, input, i, j):
    qty = 0
    if plant != input[i][j-1] or j == 0:
        qty += 1
    if plant != input[i][j+1] or j == len(input):
        qty += 1
    if plant != input[i-1][j] or i == 0:
        qty +=1
    if plant != input[i+1][j] or i < len(input[0]):
        qty += 1
    print(f"Plant {plant} at {(i, j)} has per {qty}")
    return qty

# def calc_perimeter(plant, input):
#     per = 0
#     #for p in area_perimeter_by_plant.keys():
#     for i in range(len(input)-1):
#         last_plant = ""
#         for j in range(len(input[0])-1):
#             while input[i][j] != last_plant:
#                 last_plan = input[i][j] 
#                 per += how_many_around(last_plan, input, i, j)
#     return per
                    
def calc_area_perimeter(input):
    for i in range(len(input)):
        last_plant = ""
        for j in range(len(input[0])):
            while input[i][j] != last_plant:
                last_plant = input[i][j]            
                area = calc_area(i, j, input, t)
                area_perimeter_by_plant[last_plant] += area
                
    
    #for p in area_perimeter_by_plant.keys():
    for i in range(len(input)-1):
        #last_plant = ""
        for j in range(len(input[0])-1):
            #while input[i][j] != last_plant:
            per = 0
            last_plant = input[i][j] 
            per = how_many_around(last_plant, input, i, j)
            
        area_perimeter_by_plant[last_plant] += per
    
                
    print(area_perimeter_by_plant)
    
    
if __name__ == '__main__':
    input = input.splitlines()
    t = transpose(input)
    calc_area_perimeter(input)