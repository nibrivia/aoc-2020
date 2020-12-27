from utils import *

raw = "".join(read_day(6, strip = False))
answers = raw.strip().split("\n\n")

s = 0
for x in answers:
    s += len(set(x.replace("\n", "")))
print(s)

s = 0
for g in answers:
    print(g)
    x = len(set.intersection(*[set(x) for x in g.split("\n")]))
    print(x)
    print()
    s+= x


print(s)

print("done")
