from utils import *

xs = [int(x) for x in read_day(9)]
window = 25

window_set = set(xs[:window])
print(len(window_set))
for i, x in enumerate(xs):
    if i < window:
        continue

    ok = False
    for a in window_set:
        if x-a in window_set and x-a != a:
            ok = True
            break

    if not ok:
        print(i, x, len(window_set))
        break

    window_set.add(x)
    window_set.remove(xs[i-25])

target = x
print(target)

# inclusive
start = 0
end = 0
cur = xs[0]
while True:
    if cur < target:
        end += 1
        cur += xs[end]
    if cur > target:
        cur -= xs[start]
        start += 1
    if cur == target:
        print(start, end, cur)
        break

print(min(xs[start:end+1]) + max(xs[start:end+1]))


print("done")
