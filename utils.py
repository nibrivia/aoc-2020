def read_day(n, strip = True):
    with open(f"day-{n}.input") as f:
        if strip:
            return [l.strip() for l in f.readlines()]
        else:
            return f.readlines()

def prod(xs):
    p = 1
    for x in xs:
        p*=x
    return p
