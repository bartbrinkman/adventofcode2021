import re
from collections import Counter
from pprint import pprint

file = open("p14-input","r")
lines = file.read().splitlines()
file.close()

# of course brute forcing it is not gonna work

p = lines[0]
r = []

for line in lines:
    matched = re.match('([A-Z]{2}) -> ([A-Z]{1})', line)
    if matched:
        r.append((matched[1], [matched[1][0] + matched[2], matched[2] + matched[1][1]]))
r = dict(r)

f = { v: 0 for v in list(r.keys()) }
f.update({ v[0]: 0 for v in list(r.keys()) })

# find pairs in zeroth step

for i in range(len(p)):
    f[p[i]] += 1
    if i < len(p) - 1:
        pp = p[i] + p[i + 1]
        f[pp] += 1

# now insert and add new pairs

for i in range(40):
    print(i)
    fc = f.copy()
    for pp, v in f.items():
        if v > 0 and pp in r:
            fc[pp] -= v
            fc[r[pp][0]] += v
            fc[r[pp][1]] += v
            fc[r[pp][0][1]] += v
    f = fc.copy()
    pprint(f)

# and deconstruct

c = []
for k, v in f.items():
    if len(k) == 1:
        c.append(v)

print(sum(c))
print(max(c) - min(c))