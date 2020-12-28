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

def iter_nb(pos, skip_zero = True):
    pos = list(pos)
    d = [-1, 0, 1]
    if len(pos) == 1:
        x = pos[0]
        xs = [[x+dx] for dx in d]
        yield from xs
        return

    px = pos[-1]
    for dx in d:
        x = px+dx
        for xs in iter_nb(pos[:-1], False):
            xs.append(x)
            if skip_zero and xs == pos:
                continue
            if skip_zero:
                yield(tuple(xs))
            else:
                yield xs


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

