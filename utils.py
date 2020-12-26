def read_day(n):
    with open(f"day-{n}.input") as f:
        return [l.strip() for l in f.readlines()]

def prod(xs):
    p = 1
    for x in xs:
        p*=x
    return p
