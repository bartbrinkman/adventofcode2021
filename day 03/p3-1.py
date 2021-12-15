import statistics
from statistics import mode

file = open("p3-input","r")
lines = file.read().splitlines()
file.close()

c = ''

for i in range(len(lines[0])):
    t = ()
    for line in lines:
        t += (line[i],)

    c += mode(t)

e = ''
for i in c:
    e += {'0': '1', '1': '0'}[i]

print(c)
print(e)

consumption = int(c, 2) * int(e, 2)

print(consumption)