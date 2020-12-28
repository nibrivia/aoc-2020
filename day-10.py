from utils import *
from collections import Counter

xs = [int(x) for x in read_day(10)]

chain = [0] + sorted(xs) + [max(xs)+3]
print(chain)



print(Counter(diff(chain)))
print(diff(chain))

from functools import lru_cache

def subchains(chain):
    diffs = diff(chain)
    subchains = []
    cur_sub = []
    for i, a in enumerate(chain):
        cur_sub.append(a)
        if i == len(diffs) or diffs[i] == 3:
            subchains.append(cur_sub)
            cur_sub = []

    return subchains

#print(subchains(chain))

chain2 = sorted([int(x) for x in """16
10
15
5
1
11
7
19
6
12
4""".split()])

def p(chain, pre = ""):
    #print(start, end)
    if len(chain) <= 1:
        return 1

    start = chain[0]
    end = chain[-1]

    ds = diff(chain)
    for d in ds:
        if d > 3:
            return 0

    if len(chain) == 2:
        return 1

    n = 0
    #print(pre, "i", chain[start:end+1], n)
    mid = len(chain)//2
    n += p(chain[:mid+1], pre + " ") * p(chain[mid:], pre + " ")
    n += p(chain[:mid] + chain[mid+1:], pre + " ") 
    #print(pre, "d", chain[start:end+1], n)
    return n

print(p(chain))

print("done")
