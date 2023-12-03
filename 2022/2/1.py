import os


class Shape:

    def __init__(self, name, opponent_code, my_code, shape_value, wins_to):
        self.name = name
        self.opponent_code = opponent_code
        self.my_code = my_code
        self.shape_value = shape_value
        self.wins_to = wins_to


shapes = {
    'Rock': Shape('Rock', 'A', 'X', 1, 'Scissors'),
    'Paper': Shape('Paper', 'B', 'Y', 2, 'Rock'),
    'Scissors': Shape('Scissors', 'C', 'Z', 3, 'Paper')
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
    opponent_code, my_code = line.split()
    for shape_name, shape in shapes.items():
        if shape.opponent_code == opponent_code:
            their_hand = shape
        if shape.my_code == my_code:
            my_hand = shape

    total_score += my_hand.shape_value
    if my_hand.wins_to == their_hand.name:
        total_score += outcomes['won']
    elif their_hand.wins_to == my_hand.name:
        total_score += outcomes['lost']
    else:
        total_score += outcomes['draw']

print(total_score)
