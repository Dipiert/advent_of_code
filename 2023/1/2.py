import re

DIGITS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
with open("1.txt") as f:
    res = 0
    for l in f.readlines():
        findings = re.findall(f'(?=({"|".join(DIGITS)}|\\d))', l)
        first = DIGITS.index(findings[0]) +1 if not findings[0].isdigit()  else findings[0]
        last  = DIGITS.index(findings[-1])+1 if not findings[-1].isdigit() else findings[-1]
        res += int(str(first)+str(last))
print(res)