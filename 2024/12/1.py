from collections import defaultdict

area_by_plant = defaultdict(int)
perimeter_by_plant = defaultdict(int)

input = """AAAA
BBCD
BBCC
EEEC
"""

input = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

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

plant_regions = {}

def regions(input, plants):
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
        plant_regions[p] = view
    print(plant_regions)

def transpose(input):
    t = []    
    for i in range(len(input)):
        row = []
        for j in range(len(input[0])):
            row.append(input[j][i])
        t.append(row)    
    return t

# def calc_area(i, j, input, t):
#     print(f"Horizontal: {input[i][j]}. Area: {input[i].count(input[i][j])}")
#     print(f"Vertical: {input[i][j]}. Area: {t[j].count(input[i][j])}")
#     print()
#     return input[i].count(input[i][j])

def calc_area(plant, input, t):
    area = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == plant:
                area += 1
    return area

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

    #if qty == 4:
    #    qty = 1 # Area == 1

    print(f"Plant {plant} at {(i, j)} has per {qty}")
    return qty
     
def calc_price(area_by_plant, perimeter_by_plant):
    price = 0
    for k in area_by_plant:
        price += area_by_plant[k] * perimeter_by_plant[k]
    return price
                    
def calc_area_perimeter(plants, input, t):
    # for i in range(len(input)):
    #     last_plant = ""
    #     for j in range(len(input[0])):
    #         while input[i][j] != last_plant:
    #             last_plant = input[i][j]            
    #             area = calc_area(i, j, input, t)
    #             print(area)
    #             area_by_plant[last_plant] += area
                
    for p in plants:
        area_by_plant[p] = calc_area(p, input, t)

    #print(f"Area: {area_by_plant}")
        
    
    for i in range(len(input)):
        for j in range(len(input[0])):
            last_plant = input[i][j] 
            around = how_many_around(last_plant, input, i, j)
            if around == 4 and "".join(input).count(input[i][j]) > 1:
                around = 1
            perimeter_by_plant[last_plant] += around  
            
    print(f"Area: {area_by_plant}")
    print("*" * 10)
    print(f"Perimeter: {perimeter_by_plant}")
    price = calc_price(area_by_plant, perimeter_by_plant)
    print(f"Price: {price}")
    
if __name__ == '__main__':
    plants = set(input)
    plants.remove('\n')
    input = input.splitlines()
    #regions(input, plants)
    t = transpose(input)
    calc_area_perimeter(plants, input, t)
