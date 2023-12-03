from itertools import cycle


class Monkey:

    def __init__(self, number, starting_items, operation, test, test_true, test_false):
        self.number = number
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.inspected = 0


m0 = Monkey(0, [79, 98], lambda x: x*19, lambda x: x % 23 == 0, 2, 3)
m1 = Monkey(1, [54, 65, 75, 74], lambda x: x+6, lambda x: x % 19 == 0, 2, 0)
m2 = Monkey(2, [79, 60, 97], lambda x: x*x, lambda x: x % 13 == 0, 1, 3)
m3 = Monkey(3, [74], lambda x: x+3, lambda x: x % 17 == 0, 0, 1)


for _round in range(10000):
    monkeys = [m0, m1, m2, m3]
    print('*' * 20)
    print(_round)
    print('*' * 20)
    for monkey in monkeys:
        while monkey.starting_items:
            worry_level = monkey.starting_items.pop(0)
        #items = monkey.starting_items
        #for worry_level in monkey.starting_items:

            #worry_level = monkey.starting_items.pop(0)
            print(f'Monkey {monkey.number} inspects an item with a worry level of {worry_level}')
            monkey.inspected += 1
            worry_level = monkey.operation(worry_level)
            print(f'Worry level updated to {worry_level}')
            #worry_level //= 3

            print(f'Monkey gets bored with item. Worry level is divided by 3 to {worry_level}')
            if monkey.test(worry_level):
                print(f'Item with worry level {worry_level} is thrown to monkey {monkey.test_true}')
                monkeys[monkey.test_true].starting_items.append(worry_level)
            else:
                print(f'Item with worry level {worry_level} is thrown to monkey {monkey.test_false}')
                monkeys[monkey.test_false].starting_items.append(worry_level)
    #for monkey in monkeys:
    #    print(f'Monkey {monkey.number}: {monkey.starting_items} ')
for monkey in monkeys:
    print(f'Monkey {monkey.number} inspected items {monkey.inspected} times ')


