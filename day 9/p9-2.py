from pprint import pprint

file = open("p9-input","r")
lines = file.read().splitlines()
file.close()

hm = [list(v) for v in lines]

lp = list()
for y in range(len(hm)):
    for x in range(len(hm[y])):
        adj = list()
        if y > 0:
            adj.append(hm[y - 1][x])
        if y < len(hm) - 1:
            adj.append(hm[y + 1][x])
        if x > 0:
            adj.append(hm[y][x - 1])
        if x < len(hm[y]) - 1:
            adj.append(hm[y][x + 1])

        if hm[y][x] < min(adj):
            lp.append([x,y])

b = [list() for v in range(len(lp))]

for i in range(len(lp)):
    s = list()
    s.append(lp[i])
    while len(s) > 0:
        p = s[0]
        x = p[0]
        y = p[1]
        s.remove(p)
        b[i].append(p)

        if y > 0:
            if int(hm[y - 1][x]) < 9:
                if [x, y - 1] not in s and [x, y - 1] not in b[i]:
                    s.append([x, y - 1])
        if y < len(hm) - 1:
            if int(hm[y + 1][x]) < 9:
                if [x, y + 1] not in s and [x, y + 1] not in b[i]:
                    s.append([x, y + 1])
        if x > 0:
            if int(hm[y][x - 1]) < 9:
                if [x - 1, y] not in s and [x - 1, y] not in b[i]:
                    s.append([x - 1, y])
        if x < len(hm[y]) - 1:
            if int(hm[y][x + 1]) < 9:
                if [x + 1, y] not in s and [x + 1, y] not in b[i]:
                    s.append([x + 1, y])

s = sorted([len(v) for v in b], key=None, reverse=True)
print(s[0] * s[1] * s[2])