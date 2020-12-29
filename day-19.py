from utils import *

raw = read_day(19)
raw1 = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba""".split("\n")
raw2 = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""".splitlines()
i = 0
while len(raw[i]) > 0:
    i += 1

rules_str = raw[:i]
print_lol(rules_str)
msgs = raw[i+1:]

rules = dict()
for r in rules_str:
    r_id, rule = r.split(": ")
    subrules = rule.split(" | ")
    final = []
    for s in subrules:
        local = None
        if '"' in s:
            s = s.replace('"', '')
            local = s
        else:
            ns = tuple([int(x) for x in s.split()])
            local = ns
        final.append(local)
    if len(final) == 1:
        rules[int(r_id)] = final[0]
    else:
        rules[int(r_id)] = final

def unpack(rules, idx, pre = ""):
    rule = rules[idx]


    if isinstance(rule, tuple):
        n = []
        for sr_id in rule:
            n.append(unpack(rules, sr_id, pre + "  "))
        if len(n) == 1:
            return n[0]
        return tuple(n)

    if isinstance(rule, str):
        return rule

    if isinstance(rule, list):
        n_or = []
        for opt in rule:
            assert isinstance(opt, tuple)
            n_opt = []
            for sr_id in opt:
                n_opt.append(unpack(rules, sr_id, pre + "  "))
            n_opt = tuple(n_opt)
            if len(n_opt) == 1:
                n_opt = n_opt[0]
            n_or.append(n_opt)
        if len(n_or) == 1:
            return n_or[0]
        return n_or

def make_regex(unpacked):
    if isinstance(unpacked, str):
        return unpacked
    if isinstance(unpacked, tuple):
        return "(" + "".join(make_regex(x) for x in unpacked) + ")"
    if isinstance(unpacked, list):
        return "("+"|".join(f"{make_regex(x)}" for x in unpacked) + ")"


print(rules[0])
#print(rules[129])
print()
#print(unpack(rules, 129))
print()
rule0_re = "^" + make_regex(unpack(rules, 0)) + "$"

import re
match_msgs = [m for m in msgs if re.match(rule0_re, m)]
print(len(match_msgs), len(msgs))

print()
print("Part 2")
rules[8] = [(42,), (42, 8)]
rules[11] = [(42, 31), (42, 11, 31)]

next_rule = max(rules.keys()) + 1
# simplify rules
for i, r in [t for t in rules.items()]:
    if isinstance(r, list):
        new_l = []
        for s in r:
            rules[next_rule] = s
            new_l.append(next_rule)
            next_rule += 1
        rules[i] = new_l

def match_grammar(rules, string, idx, partial = False, pre = ""):
    if isinstance(string, list):
        rems = []
        for ss in string:
            res, rem = match_grammar(rules, ss, idx, partial, pre)
            if res:
                rems.append(rem)
        if len(rems) > 0:
            return True, rems
        else:
            return False, ""

    r = rules[idx]
    #print(pre, f"{idx}: {r}{'...' if partial else ''} '{string}'")

    match = False
    rem = ""
    if isinstance(r, list):
        # TODO what if multiple subrules match?
        rems = []
        for s in r:
            res, rem = match_grammar(rules, string, s, partial, "  " + pre)
            if res:
                match = True
                rems.append(rem)
        rem = rems

    if isinstance(r, str):
        if partial:
            match = string.startswith(r)
            rem = [string[len(r):]]
        else:
            match = string == r
            rem = [""]

    if isinstance(r, tuple):
        match = True
        rem = string
        for i, s in enumerate(r):
            local_partial = True
            if i == len(r) - 1:
                local_partial = False or partial

            res, rem = match_grammar(rules, rem, s, local_partial, "  " + pre)

            # if anyone fails, return False
            if not res:
                match = False
                rem = string
                break


    #if match:
        #print(pre, f"{idx}: \033[1;32mTrue\033[0m, {rem}")
    #else:
        #print(pre, f"{idx}: \033[1;31mFalse\033[0m")

    return match, rem


match_msgs = [m for m in msgs if match_grammar(rules, m, 0)[0]]
print()
print(match_grammar(rules, msgs[4], 0, pre = "|"))
print()

print(len(match_msgs), len(msgs))
print_lol(match_msgs)




print("done")
