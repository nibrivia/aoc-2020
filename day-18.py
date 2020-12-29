from utils import *

hwk = read_day(18)
#hwk = ["1 + 2 * 3 + 4 * 5 + 6", "1 + (2 * 3) + (4 * (5 + 6))"]
exprs = [l.replace("(", " ( ").replace(")", " ) ").split() for l in hwk]



def eval(tokens, pre = ">"):
    acc = None
    op = None
    expect_val = True

    i = 0
    while i < len(tokens):
        t = tokens[i]
        if expect_val:
            if t == "(":
                val, d = eval(tokens[i+1:], "  " + pre)
                i += d 
            else:
                val = int(t)

            if op == "+":
                acc += val
                op = None
            if op == "*":
                acc *= val
                op = None
            if acc is None:
                acc = val

        else:
            if t == ")":
                return acc, i + 1
            else:
                op = t

        expect_val = not expect_val
        i += 1
    return acc

ress = [eval(e) for e in exprs]
print(sum(ress))

def full_parse(tokens):
    parsed = []
    i = 0
    while len(tokens) > 0:
        t = tokens.pop(0)
        if t == ")":
            return parsed, tokens
        if t == "(":
            embed, tokens = full_parse(tokens)
            parsed.append(embed)
        else:
            parsed.append(t)
    return parsed

def full_eval(tokens):
    for i, t in enumerate(tokens):
        if isinstance(t, list):
            tokens[i] = full_eval(t)

    while "+" in tokens:
        for i, t in enumerate(tokens):
            if t == "+":
                a = int(tokens[i-1])
                b = int(tokens[i+1])

                res = a+b

                tokens[i] = res
                tokens.pop(i+1)
                tokens.pop(i-1)
                break
    
    #Should only have products left...
    ns = [int(x) for x in tokens[0::2]]

    return prod(ns)

ress = [full_eval(full_parse(e)) for e in exprs]
print(sum(ress))

print("done")
