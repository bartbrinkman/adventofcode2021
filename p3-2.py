import statistics
from statistics import multimode

file = open("p3-input","r")
lines = file.read().splitlines()
file.close()

o2 = lines.copy()
co2 = lines.copy()

for char in range(len(lines[0])):

    t = ()
    for line in o2:
        t += (line[char],)
    mm = multimode(t)
    c = mm[0]
    if len(mm) > 1:
        c = '1'

    if len(o2) > 1:
        o2 = [i for i in o2 if i[char] != c]

    t = ()
    for line in co2:
        t += (line[char],)
    mm = multimode(t)
    c = mm[0]
    if len(mm) > 1:
        c = '1'

    if len(co2) > 1:
        co2 = [i for i in co2 if i[char] == c]

print(int(o2[0], 2) * int(co2[0], 2))
