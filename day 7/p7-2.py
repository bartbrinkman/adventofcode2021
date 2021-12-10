file = open("p7-input","r")
crab = file.read().split(',')
file.close()
crab = [int(v) for v in crab]
# crab = [16,1,2,0,4,2,7,1,2,14]

# optimization problem, brute forcing it again, might be really bad idea

fc = dict()
for pos in range(min(crab), max(crab) + 1):
    print(str(pos) + '/' + str(max(crab) + 1))
    fc[pos] = 0
    for i in range(len(crab)):
        fuel = crab[i] - pos
        if fuel < 0:
            fuel = 0 - fuel
        fc[pos] += sum(range(1, fuel + 1))

print(fc[min(fc, key=fc.get)])