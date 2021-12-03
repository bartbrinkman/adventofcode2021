x = 0
y = 0 # depth
a = 0 # aim

file = open("p2-input","r")
lines = file.read().splitlines()
file.close()

for line in lines:
    op = line.split()[0]
    val = int(line.split()[1])
    if op == 'forward':
        x += val
        y += (a * val)
    if op == 'down': a += val
    if op == 'up': a -= val

print(x, y)
print(x * y)