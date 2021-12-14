import re
from collections import Counter

file = open("p14-example","r")
lines = file.read().splitlines()
file.close()

p = lines[0]
r = []

for line in lines:
    matched = re.match('([A-Z]{2}) -> ([A-Z]{1})', line)
    if matched:
        r.append((matched[1], matched[2]))

r = dict(r)

# find pairs first, then insert and shift

for n in range(10):
    m = 0
    for i in range(len(p)):
        if i == len(p) - 1:
            continue
        pp = p[i] + p[i + 1]
        if pp in r:
            m += 1

    i = 0
    for k in range(m):
        pp = p[i] + p[i + 1]
        if pp in r:
            p = p[:i + 1] + r[pp] + p[i + 1:]
            i += 1
        i += 1

    print(Counter(list(p)))

p = Counter(list(p))
print (p[max(p, key=p.get)] - p[min(p, key=p.get)])

# print(p)