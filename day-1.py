from utils import *

expenses = set([int(x) for x in read_day(1)])

# part A
for entry in expenses:
    if 2020-entry in expenses:
        print(f"{entry} * {2020-entry} = {entry*(2020-entry)}")
        break


# part B

for entry_1 in expenses:
    for entry_2 in expenses:
        entry_3 = 2020-entry_1-entry_2
        if entry_3 in expenses:
            print(entry_1, entry_2, entry_3, 
                    entry_1 * entry_2 * entry_3)
            break

print("done")

