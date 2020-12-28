def read_day(n, strip = True):
    with open(f"day-{n}.input") as f:
        if strip:
            return [l.strip() for l in f.readlines()]
        else:
            return f.readlines()

def print_lol(lol):
    for l in lol:
        print(l)

def prod(xs):
    p = 1
    for x in xs:
        p*=x
    return p

def diff(xs):
    p = xs[0]
    diffs = []
    for x in xs[1:]:
        diffs.append(x-p)
        p = x
    return diffs

from math import gcd
def lcm(x, y):
    return x*y//gcd(x,y)

