def read_day(n):
    with open(f"day-{n}.input") as f:
        return [l.strip() for l in f.readlines()]
