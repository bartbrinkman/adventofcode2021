file = open("p6-input","r")
fish = file.read().split(',')
# fish = [3,4,3,1,2]
file.close()

bucket = [0 for i in range(9)]
for i in range(len(fish)):
    bucket[int(fish[i])] += 1

for d in range(256):
    day = [0 for i in range(9)]
    for i in range(9):
        if i == 0:
            day[6] += bucket[i]
            day[8] += bucket[i]
        if i > 0:
            day[i - 1] += bucket[i]
    bucket = day

print(sum(bucket))