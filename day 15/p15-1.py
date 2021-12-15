from pprint import pprint
from decimal import Decimal

file = open("p15-example","r")
lines = file.read().splitlines()
file.close()

# thinking about sort of df search with only down or right movement

grid = [[int(x) for x in y] for y in lines]
start = (0,0)
stop = (len(grid[len(grid) - 1]) - 1, len(grid) - 1)

def dfs(grid, node, stop, risk = 0, route = [], nodes = [], lowest = Decimal('Infinity')):
    x, y = node
    if node != (0, 0):
        risk += grid[y][x]

    if (node == stop):
        if risk < lowest:
            lowest = risk
        return lowest

    if lowest > 0 and risk > lowest:
        return lowest

    adjs = []
    if x < len(grid[y]) and y + 1 < len(grid): # b
        adjs.append((x, y + 1))
    if x + 1 < len(grid[y]) and y < len(grid): # l
        adjs.append((x + 1, y))
    if len(adjs) == 0:
        return lowest

    route.append(node)

    for adj in adjs:
        lowest = dfs(grid, adj, stop, risk, route.copy(), nodes, lowest)

    return lowest

lowest = dfs(grid, start, stop)
print(lowest)
