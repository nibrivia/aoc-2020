from utils import *
from math import cos, sin, pi

dirs = read_day(12)
dirs2 = """F10
N3
F7
R90
L90
L180
L270
L360
L0
R0
R90
R270
R360
F11""".split("\n")

x, y = (0, 0)
angle_e = 0
for inst in dirs:
    op, val = inst[0], int(inst[1:])
    if op == "E":
        x += val
    if op == "W":
        x -= val

    if op == "N":
        y += val
    if op == "S":
        x -= val

    if op == "R":
        angle_e -= val
    if op == "L":
        angle_e += val

    if op == "F":
        x += round(val * cos(angle_e/180*pi))
        y += round(val * sin(angle_e/180*pi))
print(x, y, angle_e)
print(abs(x)+abs(y))

x, y = (0, 0)
w_x, w_y = (10, 1)
for inst in dirs:
    print(f"{(x,y)} W{(w_x, w_y)}")
    print(inst)
    op, val = inst[0], int(inst[1:])
    if op == "E":
        w_x += val
    if op == "W":
        w_x -= val

    if op == "N":
        w_y += val
    if op == "S":
        w_y -= val

    if op == "R":
        val = -val
        op = "L"
    if op == "L":
        val = val/180*pi
        t_w_x = w_x * round(cos(val)) - w_y * round(sin(val))
        t_w_y = w_x * round(sin(val)) + w_y * round(cos(val))
        w_x, w_y = t_w_x, t_w_y

    if op == "F":
        x += w_x*val
        y += w_y*val

print(x, y, w_x, w_y)
print(abs(x) + abs(y))


print("done")
