from utils import *

state_raw = [list(l) for l in read_day(17)]
state_raw2 = [list(l) for l in """.#.
..#
###""".split("\n")]

state = set()
for x, row in enumerate(state_raw):
    for y, cell in enumerate(row):
        if cell == "#":
            state.add((x, y, 0))
print(state)

n = 0
for pos in iter_nb((0, 10, 20)):
    print(pos)
    n += 1
print(n)

def ds(pos):
    yield from iter_nb(pos)

def n_active(state, pos):
    n_active = 0
    for nb in ds(pos):
        if nb in state:
            n_active += 1
    return n_active

def iter_rect(state, pad = 1):
    xs, ys, zs = zip(*state)
    for x in range(min(xs)-pad, max(xs)+1+pad):
        for y in range(min(ys)-pad, max(ys)+1+pad):
            for z in range(min(zs)-pad, max(zs)+1+pad):
                yield (x, y, z)

def step(state, nb_fn = iter_rect):
    new_state = state.copy()

    for pos in nb_fn(state):
        nb = n_active(state, pos)
        if pos in state and (nb < 2 or nb > 3):
            new_state.remove(pos)
        if pos not in state and nb == 3:
            new_state.add(pos)
    return new_state

for _ in range(6):
    state = step(state)
print(len(state))

state = set()
for x, row in enumerate(state_raw):
    for y, cell in enumerate(row):
        if cell == "#":
            state.add((x, y, 0, 0))

def iter_rect4(state, pad = 1):
    xs, ys, zs, bs = zip(*state)
    for x in range(min(xs)-pad, max(xs)+1+pad):
        for y in range(min(ys)-pad, max(ys)+1+pad):
            for z in range(min(zs)-pad, max(zs)+1+pad):
                for a in range(min(bs)-pad, max(bs)+1+pad):
                    yield (x, y, z, a)

for _ in range(6):
    state = step(state, iter_rect4)
print(len(state))


