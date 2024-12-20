# part2 missing
from pathlib import Path
from collections import defaultdict

input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

def get_file_as_str(path='input.txt'):
    p = Path(__file__).with_name(path)

    with p.open("r") as f:
        file = f.read()
        
    return file

#input = get_file_as_str()

def rules_and_updates(lines):
    rules = []
    updates = []
    for l in lines:
        if "|" in l:
            rules.append(l)
        elif l == '':
            continue
        else:
            updates.append(l)
    print(f"#Rules: {len(rules)}")
    return rules, updates

def get_relevant_rules(rules, updates):
    relevant_rules = []
    for u in updates:
        for n in u.split(","):
            for r in rules:
                if n in r:
                    if r.split("|")[0] in u and r.split("|")[1] in u: 
                        relevant_rules.append(r)
    return set(relevant_rules)

def get_relevant_rules_for_update(rules, update):
    relevant_rules = []
    for n in update.split(","):
        for r in rules:
            if n in r:
                if r.split("|")[0] in update and r.split("|")[1] in update: 
                    relevant_rules.append(r)
    return set(relevant_rules)

def is_valid_update(u, relevant_rules):
    ordered = []              
    numbers = u.split(",")
    valid = True
    for n in numbers:
        pre = []
        post = []
        for r in relevant_rules:
            if n in r:
                pre.append(r.split("|")[0])
                post.append(r.split("|")[1])            
 
        if ordered == []:
            if n not in post:
                ordered.append(n)
                continue
        else:
            for on in ordered:
                for r in relevant_rules:
                    if n + "|" + on in relevant_rules:
                        return False
            ordered.append(n)
    return len(numbers) == len(ordered)
                        
def first_part(valid_updates):
    answer = 0
    for vu in valid_updates:
        numbers = vu.split(",")
        numbers = [int(n) for n in numbers]
        answer += numbers[len(numbers) // 2]
    print(answer)  

def order(u, relevant_rules):
    ordered = []
    numbers = u.split(",")
    rules_per_n = defaultdict(list)
    #for n in numbers:
    #    if ordered == []:
    #        ordered.append(n)
    #        continue
    for r in relevant_rules:
        if n in r:
            rules_per_n[n].append(r)
            #pre = r.split("|")[0]
            #post = r.split("|")[1]
            #print(f"Rules where {n} is: {r}")
            #if n == pre and post in ordered:
            #    ordered.insert(ordered.index(post), n)
            #if n == post and pre in ordered:
            #    ordered.insert(ordered.index(pre), n)
    from pprint import pprint as pp
    pp(rules_per_n)
    #print(ordered)


    #print(u, relevant_rules)

if __name__ == '__main__':
    valid_updates = []
    lines = input.split("\n")
    rules, updates = rules_and_updates(lines)
    for u in updates:
        relevant_rules = get_relevant_rules_for_update(rules, u)
        valid = is_valid_update(u, relevant_rules)
        if valid:
            valid_updates.append(u)
        else:
            order(u, relevant_rules)
    #first_part(valid_updates)
    #second_part(to_order, relevant_rules)
                 
        