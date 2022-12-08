import string
import numpy as np
import copy
from axl_legacy_reader import txt2Array


def day_one():
    with open("inputs/day_one-input.dat", 'r') as f:
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
    with open("inputs/day_two-input.dat", 'r') as f:
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
    with open("inputs/day_three-input.dat", 'r') as f:
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

def day_four():
    mylist = [row.split(',') for row in txt2array("inputs/day_four-input.dat")]

    part1_count = 0
    part2_count = 0
    for elf1, elf2 in mylist:
        a,b = list(map(int,elf1.split('-')))
        elf1_section = {i for i in range(a,b+1)}
        
        a,b = list(map(int,elf2.split('-')))
        elf2_section = {i for i in range(a,b+1)}

        section_overlap = elf1_section & elf2_section

        # In how many assignment pairs does one range fully contain the other? 
        if section_overlap == elf1_section or section_overlap == elf2_section:
            part1_count += 1

        # In how many assignment pairs do the ranges overlap?
        if section_overlap:
            part2_count += 1

    print(f"part one: {part1_count}")
    print(f"part two: {part2_count}")

def day_five():
    with open("inputs/day_five-input.dat", 'r') as f:
        file = f.read()

    stacks, instructions = file.split('\n\n')
    N = int(stacks.splitlines()[-1].split()[-1])
    stacks = stacks.splitlines()[:-1]
    instructions = instructions.splitlines()

    stack_list = [[] for i in range(N)]

    for row in stacks[::-1]:
        for i, char in enumerate(row[::4]):
            if char == '[':
                stack_list[i].append(row[i*4:i*4+3])

    stack_list_1= copy.deepcopy(stack_list)
    stack_list_2= copy.deepcopy(stack_list)
    
    instruction_list = [list(map(int,row.split()[1::2])) 
                        for row in instructions]
    
    # move n from a to b
    for n,a,b in instruction_list:
        boxes = stack_list_2[a-1][-n:]
        stack_list_2[b-1] += boxes
        del stack_list_2[a-1][-n:]
        for i in range(n):
            box = stack_list_1[a-1][-1]
            stack_list_1[b-1].append(box)
            stack_list_1[a-1].pop()
    
    message = "".join([stack[-1][1] for stack in stack_list_1])
    print(f"part one: {message}")
    message2 = "".join([stack[-1][1] for stack in stack_list_2])
    print(f"part two: {message2}")

def day_six():
    datastream = txt2array("inputs/day_six-input.dat")
    part1 = 4
    part2 = 14
    for data in datastream:
        for i,e in enumerate(data):
            j = i+1
            seq = set(data[j-part1:j])
            if len(seq) == part1:
                print(f"part one: {i+1}")
                break
    
    for data in datastream:
        for i,e in enumerate(data):
            j = i+1
            seq = set(data[j-part2:j])
            if len(seq) == part2:
                print(f"part two: {i+1}")
                break

def day_seven_good_try():
    # test works
    with open("inputs/day_seven-test.dat",'r') as f:
        asd = f.read().splitlines()

    filesystem = {}
    directory = '/'
    dirsum = 0
    parent = {}
    for row in asd:
        a = row.split()
        if a[0] == '$':
            # command
            if a[1] == 'cd':
                # change directory

                if a[2] == '..':
                    directory = parent[directory]

                else:
                    new_directory = a[2]
                    parent[new_directory] = directory
                    filesystem[new_directory] = []
                    
                    directory = new_directory
            
            if a[1] == 'ls':
                # list directory items
                pass

        
        if a[0] == 'dir':
            # directory
            filesystem[directory].append(a[1])

        if a[0].isdigit():
            # file
            filesystem[directory].append(a[0])

    dirsizes = {}
    for key,value in filesystem.items():
        # print(f"{key}: {value}")
        digits = [a.isdigit() for a in value]

        if all(digits):
            dirsum = sum([int(a) for a in np.array(value)[digits]])
            dirsizes[key] = dirsum

    # print('---')
    
    done = False
    stop = 0
    while not done:
        if stop == 10:
            print("stopped")
            break
        stop += 1

        donetest = []
        for key,value in filesystem.items():
            digits = [a.isdigit() for a in value]
            donetest.append(all(digits))

            if not all(digits):
                for i,val in enumerate(value):
                    if not val.isdigit():
                        if val in dirsizes:
                            value[i] = str(dirsizes[val])
                            filesystem[key] = value

                            digits2 = [a.isdigit() for a in value]
                            if all(digits2):
                                dirsum = sum([int(a) 
                                        for a in np.array(value)[digits2]])
                                dirsizes[key] = dirsum

        done = all(donetest)
    
    N = 100000
    total = 0
    for key,value in filesystem.items():
        print(f"{key}: {value}")
        dirsum = sum([int(val) for val in value])
        if dirsum<=N:
            total += dirsum
    
    print(f"{total=}")

def day_seven():
    # use linked list
    class Directory():
        def __init__(self,directory_name):
            self.name = directory_name
            self.parent = None
            self.size = 0
            self.dirs = {}
            self.filesizes = []
        
        def ls(self):
            for key, value in self.dirs.items():
                print(f"dir {key}")
            for file in self.filesizes:
                print(file)

    class Filesystem():
        def __init__(self,root):
            self.root = root
            self.directories = {"dir0": root}
            self.i = 1

        def add_dir(self,dir):
            self.directories[f"dir{self.i}"] = dir
            self.i += 1

        def print_system(self):
            for key,value in self.directories.items():
                print(f"{value.name}:")
                value.ls()

    with open("inputs/day_seven-input.dat",'r') as f:
        asd = f.read().splitlines()

    root = Directory('/')
    filesystem = Filesystem(root)

    for row in asd:
        a = row.split()
        if a[0] == '$':
            # command
            if a[1] == 'cd':
                # change directory
                move_to = a[2]
                if move_to == '..':
                    directory = directory.parent
                
                elif move_to == '/':
                    directory = filesystem.root
                
                else:
                    directory = directory.dirs[move_to]
            
            if a[1] == 'ls':
                # list directory items
                pass

        
        if a[0] == 'dir':
            # directory
            if a[1] not in directory.dirs:
                new_dir = Directory(a[1])
                new_dir.parent = directory
                filesystem.add_dir(new_dir)
                directory.dirs[new_dir.name] = new_dir

        if a[0].isdigit():
            # file
            if a[0] not in directory.filesizes:
                directory.filesizes.append(a[0])
    
    # filesystem.print_system()

    done = False
    stop = 0
    while not done:
        if stop == 100:
            print("stopped")
            break
        stop += 1

        donetest = []
        for _, dir in filesystem.directories.items():
            if dir.dirs == {}:
                donetest.append(True)
                dir.size = sum([int(file) for file in dir.filesizes])
            
            else:
                donetest.append(False)
                rmdirs = []
                for name,subdir in dir.dirs.items():
                    if subdir.size:
                        dir.filesizes.append(str(subdir.size))
                        rmdirs.append(name)
                
                for name in rmdirs:
                    del dir.dirs[name]

        done = all(donetest)

    N = 100000
    disksize = 70000000
    free_space = 30000000 - (disksize - filesystem.root.size)
    
    total1 = 0
    pot_dirs = []
    for _, dir in filesystem.directories.items():
        if dir.size <=N:
            total1 += dir.size
        
        if dir.size >= free_space:
            pot_dirs.append(dir.size)

    print(f"part one: {total1}")
    print(f"part two: {min(pot_dirs)}")

def day_eight():
    class Tree:

        def __init__(self,height, i, j):
            self.height = height
            self.visible = None
            self.coords = (i,j)
            self.scenic_score = 0

        def check_visibility(self):
            i,j = self.coords

            up = forest.T[j][i-1::-1]
            down = forest.T[j][i+1:]
            left = forest[i][j-1::-1]
            right = forest[i][j+1:]

            # part two
            scenic_score = 1
            for direction in [up,left,right,down]:
                for k,tree in enumerate(direction):
                    if tree.height >= self.height:
                        break

                scenic_score *= k+1

            self.scenic_score = scenic_score

            # part one
            for direction in [up,left,right,down]:
                blocked = False
                for tree in direction:
                    if tree.height >= self.height:
                        blocked = True
                        break
                
                if blocked:
                    continue

                self.visible = True
                return
            
            self.visible = False


    input_ = txt2Array("inputs/day_eight-input.dat")
    tree_heights = [[int(a) for a in row] for row in input_]

    forest = [[Tree(height,i,j) for j,height in enumerate(row)]
                for i,row in enumerate(tree_heights)]

    forest = np.array(forest)
    visible_count = 0
    borders = set([*forest[0],*forest[-1],*forest.T[0],*forest.T[-1]])

    for tree in borders:
        tree.visible = True
        visible_count += 1

    best_score = 0
    for row in forest[1:-1]:
        for tree in row[1:-1]:
            tree.check_visibility()
            visible_count += tree.visible
            score = tree.scenic_score
            if score > best_score:
                best_score = score

    print(f"visible trees: {visible_count}") # 655 too low, 1963 too high
    print(f"highest scenic score: {best_score}")