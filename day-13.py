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
print(prod(valid_ids))

x = 0
while x < prod(valid_ids):
    x += 937

print("done")
