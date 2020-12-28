from utils import *
import parse

def i2b(i):
    return "{0:b}".format(i).zfill(36)

def b2i(b):
    return int(b, 2)

def sub(val, mask):
    val_s = i2b(val)
    new_s = list(val_s)
    for i, (v, m) in enumerate(zip(val_s, mask)):
        if m == "X":
            continue
        else:
            new_s[i] = m
    return b2i("".join(new_s))

x = read_day(14)

mask = "X"*32
mem = dict()
for line in x:
    #print(line, mask)
    if "mask" in line:
        mask = line.split(" = ")[1]
    if "mem" in line:
        addr, val = parse.parse("mem[{:d}] = {:d}", line)
        mem[addr] = sub(val, mask)

print(sum(mem.values()))

def gen_addr(addr):
    if "X" not in addr:
        return [addr]
    addrs = []

    for i, c in enumerate(addr):
        if c == "X":
            a_c = list(addr)
            a_c[i] = "0"
            addrs.extend(gen_addr("".join(a_c)))

            a_c = list(addr)
            a_c[i] = "1"
            addrs.extend(gen_addr("".join(a_c)))

            #only do first "X"
            break
    return addrs





def sub2(addr, mask):
    addr_s = i2b(addr)
    new_s = list(addr_s)
    for i, (a, m) in enumerate(zip(addr_s, mask)):
        if m == "X":
            new_s[i] = "X"
        if m == "1":
            new_s[i] = "1"

    return [b2i(a) for a in gen_addr("".join(new_s))]

print(sub2(42, "000000000000000000000000000000X1001X"))


mask = ""
mem = dict()
for line in x:
    #print(line, mask)
    if "mask" in line:
        mask = line.split(" = ")[1]
    if "mem" in line:
        addr, val = parse.parse("mem[{:d}] = {:d}", line)
        for a in sub2(addr, mask):
            mem[a] = val

print(sum(mem.values()))



print("done")
