from utils import *

pps_raw = "".join(read_day(4, strip = False))
pps = pps_raw.split("\n\n")

req_fields = ["byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        #"cid",
    ]

n_valid = 0
for p in pps:
    ok = all(f in p for f in req_fields)
    n_valid += ok
print(n_valid)

def valid_height(h_str):
    x = int(h_str[:-2])
    if "in" in h_str:
        return 59 <= x <= 76
    if "cm" in h_str:
        return 150 <= x <= 193
    return False

req_fields = [
        ("byr", "\d{4}", lambda x: 1920 <= int(x) <= 2002),
        ("iyr", "\d{4}", lambda x: 2010 <= int(x) <= 2020),
        ("eyr", "\d{4}", lambda x: 2020 <= int(x) <= 2030),
        ("hgt", "\d{2,3}(in|cm)", valid_height),
        ("hcl", "#[0-9a-f]{6}", lambda _: True),
        ("ecl", "(amb|blu|brn|gry|grn|hzl|oth)", lambda _: True),
        ("pid", "^\d{9}$", lambda _: True),
    ]

pps_invalid = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007""".split("\n\n")

pps_valid = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719""".split("\n\n")

import re
n_valid = 0
for p in pps:
    is_valid = True

    fields = dict()
    for fv in p.split():
        f, v = fv.strip().split(":")
        fields[f] = v

    p_str = ""

    p_str += p + "\n"
    # Check every field
    for (f, regex, test) in req_fields:
        # Field should exist
        if f not in fields:
            is_valid = False
            break

        match = re.match(regex, fields[f])
        if match and test(fields[f]):
            # regex and valid passs
            p_str += " ".join(("\033[1;32m", f, fields[f], "\033[0;0m")) + "\n"
            pass
        else:
            # something isn't right, break out
            is_valid = False
            p_str += " ".join(("\033[1;31m", f, fields[f], "\033[0;0m")) + "\n"
            break

    # Done checking things, reset
    if is_valid:
        print(f"{p_str}\033[1;32mok\033[0;0m")
        n_valid += 1
    else:
        print("\033[1;31mno\033[0;0m")
    print()

print(n_valid)
print("done")
