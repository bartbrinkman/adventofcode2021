x = 0
y = 0 # depth

file = open("p2-input","r")
lines = file.read().splitlines()
file.close()

for line in lines:
    op = line.split()[0]
    val = int(line.split()[1])
    if op == 'forward': x += val
    if op == 'down': y += val
    if op == 'up': y -= val

print(x, y)
print(x * y)