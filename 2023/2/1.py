import operator
import re
from functools import reduce
import operator
def second():
    total = 0
    with open("input.txt") as f:
        for l in f.readlines():
            m = re.match("Game (.+):(.+)", l)
            if m:
                maxs = {"red": 0, "green": 0, "blue": 0}
                ocurrences = m.group(2)
                sets = ocurrences.split(";")
                for s in sets:
                    record = s.split(",")
                    for r in record:
                        m = re.match("(.+) (blue|red|green)", r)
                        if m:
                            how_many = int(m.group(1))
                            color = m.group(2)
                            if how_many > maxs[color]:
                                maxs[color] = how_many
            total += reduce(operator.mul, (int(v) for _, v in maxs.items()), 1)
    print(total)

def first():
    possible_games = set()
    rule = {"red": 12, "green": 13, "blue": 14}
    res = 0
    with open("input.txt") as f:
        for l in f.readlines():
            m = re.match("Game (.+):(.+)", l)
            if m:
                current = {"red": 0, "green": 0, "blue": 0}
                current["id"] = m.group(1)
                possible_games.add(current["id"])
                ocurrences = m.group(2)
                sets = ocurrences.split(";")
                for s in sets:
                    record = s.split(",")
                    for r in record:
                        m = re.match("(.+) (blue|red|green)", r)
                        if m:
                            how_many = int(m.group(1))
                            color = m.group(2)
                            current[color] = how_many
                    if current["red"] > rule["red"] or current["green"] > rule["green"] or current["blue"] > rule["blue"]:
                        print(f"Will remove Game {current["id"]}: {current}")
                        possible_games.remove(current["id"])
                        break
    print(sum(int(n) for n in possible_games))

second()