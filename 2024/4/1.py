#working on part2
from pathlib import Path
import re

do = True

def get_file_as_str(path='input.txt'):
    p = Path(__file__).with_name(path)

    with p.open("r") as f:
        file = f.read()
        
    return file

def count_horizontal(row, j, backward=False):
    to_search = 'MAS' if not backward else 'AMX'
    if row[j+1:j+4] == to_search:
        #print(f"Found horizontal: {row[j:j+4]}")
        return 1
    return 0

def count_vertical(rows, i, j, backward=False):
    to_search = 'MAS' if not backward else 'AMX'
    try:
        if ''.join([rows[i+k][j] for k in range(1, 4)]) == to_search:
            #print("Found vertical")
            return 1
    except IndexError:
        pass
    return 0
    
def count_brtl(rows, i, j):
    """
    S . . .
    . A . .
    . . M .
    . . . X
    """
    ret = 0
    try:
        if i >= 3 and j >= 3:
            if ''.join([rows[i-k][j-k] for k in range(1, 4)]) == 'MAS':
                print(f"X building BRTL at i={i}, j={j}")
                ret = 1
    except IndexError:
        ret = 0
    finally:
        return ret
    
def count_bltr(rows, i, j):
    """
    . . . S
    . . A .
    . M . .
    X . . .
    """
    ret = 0
    try:
        if i >= 3 and j-3 <= len(rows[i]):
            if ''.join([rows[i-k][j+k] for k in range(1, 4)]) == 'MAS':
                print(f"X building BLTR at i={i}, j={j}")
                ret = 1
    except IndexError as e:
        ret = 0
    return ret 
    
def count_trbl(rows, i, j):
    """
    . . . X
    . . M .
    . A . .
    S . . .
    """
    ret = 0
    try:
        if i+3 < len(rows) and j >= 3:
            if ''.join([rows[i+k][j-k] for k in range(1, 4)]) == 'MAS':
                print(f"X building TRBL at i={i}, j={j}")
                ret = 1
    except IndexError:
        ret = 0
    return ret

def count_tlbr(rows, i, j):
    """
    X . . .
    . M . .
    . . A .
    . . . S
    """
    ret = 0        
    try:
        if i+3 < len(rows) and j+3 < len(rows[i]):
            if ''.join([rows[i+k][j+k] for k in range(1, 4)]) == 'MAS':
                print(f"X building TLBR at i={i}, j={j}")
                ret = 1
    except IndexError:
        ret = 0
    return ret



  

def count(rows):
    vertical = 0
    vertical_backwards = 0
    horizontal = 0
    horizontal_backwards = 0
    brtl = 0
    bltr = 0
    trbl = 0
    tlbr = 0
    count = 0
    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            if c == 'X':
                horizontal += count_horizontal(row, j)
                vertical += count_vertical(rows, i, j)
                brtl += count_brtl(rows, i, j)
                bltr += count_bltr(rows, i, j)
                trbl += count_trbl(rows, i, j)
                tlbr += count_tlbr(rows, i, j)
            if c == 'S':    
                horizontal_backwards += count_horizontal(row, j, True)   
                vertical_backwards += count_vertical(rows, i, j, True)               

    print(f"Horizontal: {horizontal}")
    print(f"Horizontal Backwards: {horizontal_backwards}")
    print(f"Vertical: {vertical}")
    print(f"Vertical Backwards: {vertical_backwards}")
    print(f"BRTL: {brtl}")
    print(f"BLTR: {bltr}")
    print(f"TRBL: {trbl}")
    print(f"TLBR: {tlbr}")
    
    count = horizontal + horizontal_backwards + vertical + vertical_backwards + brtl + bltr + trbl + tlbr
    print(count) # 2000 is too low, 2515 is too high, 2510 is not, 2506 is not
              
def part2(rows):
    count = 0
    for i, row in enumerate(rows):
        for j, c in enumerate(row):
            if c == 'M':
                try:
                    if rows[i+1][j+1] == 'A' and rows[i+2][j+2] == 'S' and rows[i][j+2] == 'S' and rows[i+2][j] == 'M':
                        count += 1
                except IndexError as e:
                    continue
    print(count)
                        
if __name__ == '__main__':
    input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
    #input = get_file_as_str()
    rows = input.splitlines()
    #count(rows)
    part2(rows)
