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
            print(hm[y][x], adj)
            lp.append(int(hm[y][x]) + 1)

print(sum(lp))
