from utils import *
import parse

password_db = read_day(2)
pwd_format = "{:d}-{:d} {}: {}"

policy_pwd = [tuple(parse.parse(pwd_format, s)) for s in password_db]

n_good = 0
for lo, hi, c, pwd in policy_pwd:
    count = pwd.count(c)
    n_good += lo <= count <= hi

print(n_good)



n_good = 0
for a, b, c, pwd in policy_pwd:
    a_c = pwd[a-1] == c
    b_c = pwd[b-1] == c
    if (a_c or b_c) and (a_c != b_c):
        n_good += 1

print(n_good)

print("done")
