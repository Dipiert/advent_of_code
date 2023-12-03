with open("1.txt") as f:
    res = 0
    for l in f.readlines():
        digits = []
        for c in l:
            if c.isdigit():
                digits.append(c)
        res += int(digits[0] + digits[-1])
print(res)