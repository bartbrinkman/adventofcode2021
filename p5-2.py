import re

file = open("p5-input","r")
lines = file.read().splitlines()
file.close()

# we're gonna brute force it (slow)

cords = []
for line in lines:
    match = re.search('(\d+),(\d+) -> (\d+),(\d+)', line)
    x1 = int(match.group(1))
    x2 = int(match.group(3))
    y1 = int(match.group(2))
    y2 = int(match.group(4))

    if x1 == x2:
        step = 1
        y2 += 1
        if (y1 > y2):
            step = -1
            y2 -= 2
        for y in range(y1, y2, step):
            cords.append(str(x1) + ',' + str(y))

    if y1 == y2:
        step = 1
        x2 += 1
        if (x1 > x2):
            step = -1
            x2 -= 2
        for x in range(x1, x2, step):
            cords.append(str(x) + ',' + str(y1))

    if x1 != x2 and y1 != y2:
        x_step = 1
        x2 += 1
        if (x1 > x2):
            x_step = -1
            x2 -= 2
        y = y1
        y_step = 1
        if (y1 > y2):
            y_step = -1
        for x in range(x1, x2, x_step):
            cords.append(str(x) + ',' + str(y))
            y += y_step

occ = 0
for cord in set(cords):
    if cords.count(cord) > 1:
        print(cord, cords.count(cord))
        occ += 1

print(occ)