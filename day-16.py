from utils import *
import parse

x = "".join(read_day(16, strip = False))
rules_raw, my_ticket, other_tickets_raw = x.split("\n\n")

rules = dict()
for line in rules_raw.split("\n"):
    print(line)
    field, a_lo, a_hi, b_lo, b_hi = parse.parse("{}: {:d}-{:d} or {:d}-{:d}", line)
    valid_a = set(x for x in range(a_lo, a_hi+1))
    valid_b = set(x for x in range(b_lo, b_hi+1))
    valid = set.union(valid_a, valid_b)
    rules[field] = valid

all_valid = set.union(*rules.values())

other_tickets = [[int(x) for x in row.split(",")] for row in other_tickets_raw.strip().split("\n")[1:]]
print(other_tickets[1])

errs = []
bad_tix = []
for i, vals in enumerate(other_tickets):
    for v in vals:
        if v not in all_valid:
            errs.append(v)
            bad_tix.append(i)

print(sum(errs))

valid_tix = [t for i, t in enumerate(other_tickets) if i not in bad_tix]
cols = [c for c in zip(*valid_tix)]
options = [set(rules.keys()) for _ in cols]

for i, col in enumerate(cols):
    for f, v in rules.items():
        all_valid = all(x in v for x in col)
        if not all_valid:
            options[i].remove(f)
options = [(s, i) for i, s in enumerate(options)]
options = sorted(options)
assgt = [None for _ in cols]

done = False
for _ in cols:
    opts, col = options[0]
    assert len(opts) == 1
    field = opts.pop()
    assgt[col] = field

    options = options[1:]
    for os, i in options:
        os.remove(field)
    options = sorted(options)
print(assgt)

my_ticket = [int(x) for x in my_ticket.split("\n")[1].split(",")]
print(my_ticket)
vals = [x for f, x in zip(assgt, my_ticket) if "departure" in f]
print(prod(vals))







print("done")
