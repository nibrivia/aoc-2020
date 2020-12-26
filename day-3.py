from utils import *

forest = read_day(3)
width = len(forest[0])

right = 3
down = 1

x = 0
y = 0

n_trees = 0
while y < len(forest):
    line = forest[y]
    cur = line[x%width]
    n_trees +=  cur == "#"
    x += right
    y += down

print(n_trees)

def count_slope_trees(forest, right, down):
    x = 0
    y = 0

    n_trees = 0
    while y < len(forest):
        line = forest[y]
        cur = line[x%width]
        n_trees +=  cur == "#"
        x += right
        y += down

    return n_trees

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
n_trees_slope = [count_slope_trees(forest, *s) for s in slopes]
print(prod(n_trees_slope))

print("done")
