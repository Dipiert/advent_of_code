from input_utils import get_file_as_str

def _get_cols():
    left = []
    right = []

    file = get_file_as_str()

    for l in file.splitlines():
        line = l.split("   ")
        print(line)
        left.append(line[0])
        right.append(line[1])
        
    return left, right

def distance():    
    left, right = _get_cols()
    _distance = 0
    
    for l, r in zip(sorted(left), sorted(right)):
        l = int(l)
        r = int(r)
        _distance += abs(l - r)
        
    print(_distance)

def similarity():
    left, right = _get_cols()
    _similarity = 0

    for n in left:
        _similarity += int(n) * right.count(n)
    print(_similarity)        
    

if __name__ == '__main__':
    #distance()
    similarity()