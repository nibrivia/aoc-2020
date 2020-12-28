from utils import *

x = read_day(13)

print(x)
earliest = int(x[0])
print(earliest)
ids = x[1].split(",")
print(ids)
valid_ids = [int(x) for x in ids if x != "x"]
print(valid_ids)

t = earliest
wait = [(id-earliest%id, id) for id in valid_ids]
print(min(wait))
m = min(wait)
print(m[0]*m[1])

# Part 2
print(prod(valid_ids))
iids = [(int(id), i) for i, id in enumerate(ids) if id != "x"]
print(iids)
iids = sorted(iids)[::-1]
print(iids)

mod, offset = iids[0]
x = mod-offset
step = mod
for mod, offset in iids[1:]:
    while x % mod != (-offset%mod):
        print(x, step, mod, offset)
        x += step
    step = lcm(mod, step)

for mod, offset in iids:
    print(x+offset, mod, offset, (x+offset)%mod)
print(x, 1068781)

x = 0
while x < prod(valid_ids):
    x += max(valid_ids)

print("done")
