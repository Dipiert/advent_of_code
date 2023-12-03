import os


class Shape:

    def __init__(self, name, opponent_code, shape_value, wins_to):
        self.name = name
        self.opponent_code = opponent_code
        self.shape_value = shape_value
        self.wins_to = wins_to


shapes = {
    'Rock': Shape('Rock', 'A', 1, 'Scissors'),
    'Paper': Shape('Paper', 'B', 2, 'Rock'),
    'Scissors': Shape('Scissors', 'C', 3, 'Paper')
}

map_need_to = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

outcomes = {
    'lost': 0,
    'draw': 3,
    'won': 6,
}

with open(os.path.join(os.path.dirname(__file__), 'input.txt')) as f:
    inp = f.read().splitlines()

total_score = 0
for line in inp:
    opponent_code, need_to = line.split()

    opponent_hand = None
    i = 0
    for shape_name, shape in shapes.items():
        if opponent_code == shape.opponent_code:
            their_hand = shape

    if map_need_to[need_to] == 'win':
        for shape_name, shape in shapes.items():
            if shape.wins_to == their_hand.name:
                my_hand = shape
    elif map_need_to[need_to] == 'lose':
        my_hand = shapes[their_hand.wins_to]
    else:
        my_hand = their_hand

    total_score += my_hand.shape_value
    if my_hand.wins_to == their_hand.name:
        total_score += outcomes['won']
    elif their_hand.wins_to == my_hand.name:
        total_score += outcomes['lost']
    else:
        total_score += outcomes['draw']

print(total_score)
