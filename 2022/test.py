import numpy as np
import random
random.seed(1)




a = [[random.randint(0,9) for i in range(1,6)] for j in range(1,6)]
a = np.array(a)

i = 2
j = 3

up = a.T[j][i-1::-1]
down = a.T[j][i+1:]
left = a[i][j-1::-1]
right = a[i][j+1:]

print(a)
dude = a[i][j] 
print(dude)


for direction,j in zip([up,left,right,down],["up","left","right","down"]):
    print(j)
    next_dir = False
    for i,tree in enumerate(direction):
        # print(f"tree{i}")
        if tree >= dude:
            next_dir = True
            break

    if next_dir:
        continue
    print("visible")

exit()
a = [1,2,3,4,5]
b = a[3:1:-1]
print(b)

exit()
for neighbour in [1,2,3,4]:
    if neighbour < 3:
        continue
    print(neighbour)

exit()
truecheck = None and True
print(truecheck)

if truecheck:
    print("lol")
exit()
counter = 0

counter += True
counter += 1
counter += False
print(counter)
exit()
a = [1,2,3]
b = a.copy()
a.pop()
print(a)
print(b)
a += b
print(a)