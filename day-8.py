from utils import *
import parse

code = read_day(8)
parsed = [line.split() for line in code]

def run_noloop(parsed, pc = 0, acc = 0):
    executed = set()
    while pc not in executed and pc < len(parsed):
        inst, val = parsed[pc]
        executed.add(pc)

        if inst == "acc":
            acc += int(val)
            pc += 1
            continue
        if inst == "jmp":
            pc += int(val)
            continue
        if inst == "nop":
            pc += 1
            continue

    return (pc, acc, executed)

pc, acc, executed = run_noloop(parsed)
print(acc)

for l in executed:
    if parsed[l][0] == "nop":
        parsed[l][0] = "jmp"
        pc, acc, _ = run_noloop(parsed)
        if pc >= len(parsed):
            print(l, pc, acc)
            break
        else:
            parsed[l][0] = "nop"

    if parsed[l][0] == "jmp":
        parsed[l][0] = "nop"
        pc, acc, _ = run_noloop(parsed)
        if pc >= len(parsed):
            print(l, pc, acc)
            break
        else:
            parsed[l][0] = "jmp"



print("done")
