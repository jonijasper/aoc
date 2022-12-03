import string
import numpy as np


def day_one():
    with open("day_one-input.dat", 'r') as f:
        contents = f.read()
    
    elf_calories = [calories.split() for calories in contents.split('\n\n')]
    total_cals = [sum(list(map(int,elf))) for elf in elf_calories]
    total_cals.sort()

    print(f"part one: {total_cals[-1]}")
    print(f"part two: {sum(total_cals[-3:])}")


def day_two():
    '''
    rock paper scissors
    A B C
    X Y Z
    '''
    with open("day_two-input.dat", 'r') as f:
        contents = f.read()

    guide = [row.split() for row in contents.split('\n')]
    
    ## part one
    scores = {"X":1,"Y":2,"Z":3}
    opponent_opts = ['A', 'B', 'C']
    me_opts = ['X', 'Y', 'Z']

    my_score = 0
    for opponent,me in guide:
        my_score += scores[me]
        
        i = me_opts.index(me)
        j = opponent_opts.index(opponent)

        if i==j:
            my_score += 3

        if opponent==opponent_opts[i-1]:
            my_score += 6
        
    print(f"part one: {my_score}")

    ## part two
    outcome_scores = {'X':0, 'Y':3, 'Z':6}
    opponent_opts = ['A', 'B', 'C']
    scores = {'A':1,'B':2,'C':3}

    my_score = 0
    for opponent,outcome in guide:
        my_score += outcome_scores[outcome]

        i = opponent_opts.index(opponent)
        if outcome=='X':
            #lose
            me = opponent_opts[i-1]

        elif outcome=='Y':
            #draw
            me = opponent_opts[i]

        else:
            #win
            me = opponent_opts[i-2]
        
        my_score += scores[me]

    print(f"part two: {my_score}")


def day_three():
    with open("day_three-input.dat", 'r') as f:
        contents = f.read().splitlines()

    mistakes = []
    for rucksack in contents:
        i = len(rucksack)//2
        a = set(rucksack[:i])
        b = set(rucksack[i:])
        mistakes.append(list(a & b)[0])

    priority = list(string.ascii_letters)
    sum_ = sum([priority.index(a)+1 for a in mistakes])
    print(f"part one: {sum_}")

    N = len(contents)//3
    ruccsacc = np.array(contents).reshape(N,3)
    
    badges = [list(set(a) & set(b) & set(c))[0] for a,b,c in ruccsacc]
    
    sum_ = sum([priority.index(a)+1 for a in badges])
    print(f"part two: {sum_}")


if __name__ == "__main__":
    day_three()
