from axl_legacy_reader import txt2Array
import numpy as np

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


with open("forest.txt", "w") as f:
    for row in forest:
        for tree in row:
            if tree.visible:
                f.write("o ")
            else:
                f.write("x ")
        f.write("\n")

print(f"visible trees: {visible_count}") # 655 too low, 1963 too high
print(f"highest scenic score: {best_score}")