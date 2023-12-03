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


m0 = Monkey(0, [66, 71, 94], lambda x: x*5, lambda x: x % 3 == 0, 7, 4)
m1 = Monkey(1, [70], lambda x: x+6, lambda x: x % 17 == 0, 3, 0)
m2 = Monkey(2, [62, 68, 56, 65, 94, 78], lambda x: x+5, lambda x: x % 2 == 0, 3, 1)
m3 = Monkey(3, [89, 94, 94, 67], lambda x: x+2, lambda x: x % 19 == 0, 7, 0)
m4 = Monkey(4, [71, 61, 73, 65, 98, 98, 63], lambda x: x*7, lambda x: x % 11 == 0, 5, 6)
m5 = Monkey(5, [55, 62, 68, 61, 60], lambda x: x+7, lambda x: x % 5 == 0, 2, 1)
m6 = Monkey(6, [93, 91, 69, 64, 72, 89, 50, 71], lambda x: x+1, lambda x: x % 13 == 0, 5, 2)
m7 = Monkey(7, [76, 50], lambda x: x*x, lambda x: x % 7 == 0, 4, 6)


for _round in range(10000):
    monkeys = [m0, m1, m2, m3, m4, m5, m6, m7]
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


