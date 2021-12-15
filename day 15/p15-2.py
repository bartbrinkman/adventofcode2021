from pprint import pprint
from decimal import Decimal

file = open("p15-input","r")
lines = file.read().splitlines()
file.close()

w = len(lines[0])
h = len(lines)

for i in range(len(lines)):
    lines[i] = lines[i] * 5

for y in range(len(lines)):
    for i in range(1, 5):
        for x in range(w):
            x = x + (w * i)
            val = int(lines[y][x])
            val += i
            if val > 9:
                val -= 9
            lines[y] = lines[y][:x] + str(val) + lines[y][x + 1:]

lines = lines * 5

for x in range(len(lines[0])):
    for i in range(1, 5):
        for y in range(w):
            y = y + (w * i)
            val = int(lines[y][x])
            val += i
            if val > 9:
                val -= 9
            lines[y] = lines[y][:x] + str(val) + lines[y][x + 1:]

grid = [[int(x) for x in y] for y in lines]

start = (0, 0)
stop = (len(grid[len(grid) - 1]) - 1, len(grid) - 1)

queue = []
dist = {}
prev = {}

for y in range(len(grid)):
    for x in range(len(grid[y])):
        node = (x, y)
        queue.append(node)
        dist[node] = Decimal('Infinity')
        prev[node] = None

dist[start] = 0

while len(queue) > 0:
    u = queue[0]
    for node in queue:
        if dist[node] < dist[u]:
            u = node

    x, y = u
    adjs = []
    if x < len(grid[y]) and y - 1 < len(grid): # t
        draft = (x, y - 1)
        if draft in queue: adjs.append(draft)
    if x < len(grid[y]) and y + 1 < len(grid): # b
        draft = (x, y + 1)
        if draft in queue: adjs.append(draft)
    if x + 1 < len(grid[y]) and y < len(grid): # l
        draft = (x + 1, y)
        if draft in queue: adjs.append(draft)
    if x - 1 < len(grid[y]) and y < len(grid): # r
        draft = (x - 1, y)
        if draft in queue: adjs.append(draft)
    for adj in adjs:
        x, y = adj
        td = dist[u] + grid[y][x]
        if td < dist[adj]:
            dist[adj] = td
            prev[adj] = u

    queue.remove(u)
    print(len(queue))

risk = 0
u = stop
while True:
    x, y = u
    risk += grid[y][x]
    u = prev[u]
    if u == start:
        break

print(risk)