file = open("p6-input","r")
fish = file.read().split(',')
file.close()
fish = [int(v) for v in fish]

for d in range(256):
    print(d)
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 7
            fish.append(8)
        fish[i] -= 1
print(len(fish))