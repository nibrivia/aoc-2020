from utils import *

raw = "1,20,8,12,0,14"
#raw = "0,3,6"
xs = [int(x) for x in raw.split(",")]
print(xs)

numbers = {x: i+1 for i, x in enumerate(xs[:-1])}
print(numbers)
turn = len(xs)
last = xs[-1]
while turn < 30000000:
    new = 0
    if last in numbers:
        new = turn-numbers[last]
        #print(f"{turn}: ({last} @{numbers[last]})")
    else:
        new = 0

    numbers[last] = turn
    turn += 1
    last = new

print(last)



print("done")
