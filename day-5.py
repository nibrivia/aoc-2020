from utils import *

seats = read_day(5)
bin_str = [s.replace("F", "0").replace("L", "0")
        .replace("B", "1").replace("R", "1") for s in seats]
seat_ids = [int(s, 2) for s in bin_str]
print(max(seat_ids))

seats = set(x for x in range(128*8))
#seats.substract(set(seat_ids))
print(seats-set(seat_ids))

print("done")
