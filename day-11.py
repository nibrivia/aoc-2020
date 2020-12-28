from utils import *

state = read_day(11)
state = [list(row.strip()) for row in state]

def iter_square(pos):
    x, y = pos

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            yield (x+dx, y+dy)

def nbor_occ(state, pos):
    n_occ = 0
    for (x, y) in iter_square(pos):
        if x < 0 or y < 0:
            continue
        try:
            n_occ += state[x][y] == "#"
        except:
            pass
    return n_occ


def iter_state(cur_state):
    tmp = cur_state[0][0]

    new_state = [[c[:] for c in row] for row in cur_state]
    new_state[0][0] = "x"
    assert cur_state[0][0] != "x"

    new_state[0][0] = tmp
    for x, row in enumerate(cur_state):
        for y, cell in enumerate(row):
            if cell == ".":
                continue

            n_occ = nbor_occ(cur_state, (x, y))
            if cell == "#" and n_occ >= 4:
                new_state[x][y] = 'L'
            if cell == "L" and n_occ == 0:
                new_state[x][y] = '#'

    return new_state

def iter_until_stable(state, iter_fn = iter_state):
    while True:
        print()
        print_state(state)
        new_state = iter_fn(state)
        if str(new_state) == str(state):
            print("oh!")
            print_state(state)
            return state
        state = new_state

def print_state(state):
    for row in state:
        print("".join(row))

print_state(state)

final_state = iter_until_stable(state)

print()
print_state(final_state)

n_occ = 0
for row in final_state:
    for cell in row:
        if cell == "#":
            n_occ += 1
print(n_occ)


def nbor_occ2(state, pos):
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)]
    x, y = pos
    n_occ = 0
    for dx, dy in dirs:
        cx, cy = x, y
        while True:
            cx, cy = cx+dx, cy+dy
            if cx < 0 or cy < 0:
                break
            if cx >= len(state) or cy >= len(state[0]):
                break

            if state[cx][cy] == "L":
                break

            if state[cx][cy] == "#":
                n_occ += 1
                break
    return n_occ


def iter_state_2(cur_state):
    tmp = cur_state[0][0]

    new_state = [[c[:] for c in row] for row in cur_state]
    new_state[0][0] = "x"
    assert cur_state[0][0] != "x"

    new_state[0][0] = tmp
    for x, row in enumerate(cur_state):
        for y, cell in enumerate(row):
            if cell == ".":
                continue

            n_occ = nbor_occ2(cur_state, (x, y))
            if cell == "#" and n_occ >= 5:
                new_state[x][y] = 'L'
            if cell == "L" and n_occ == 0:
                new_state[x][y] = '#'

    return new_state


final_state = iter_until_stable(state, iter_state_2)

print()
print_state(final_state)

n_occ = 0
for row in final_state:
    for cell in row:
        if cell == "#":
            n_occ += 1
print(n_occ)

print("done")
