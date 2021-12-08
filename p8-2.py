import re

file = open("p8-input","r")
lines = file.read().splitlines()
file.close()

# lets go with a heuristic for this one

nums = []
for i in range(len(lines)):
    pat = lines[i].split(' | ')[0].split()
    pat = ["".join(sorted(v)) for v in pat]

    dmap = {}
    for seq in pat.copy():
        if len(seq) == 2:
            dmap[1] = seq
            pat.remove(seq)

        if len(seq) == 3:
            dmap[7] = seq
            pat.remove(seq)

        if len(seq) == 4:
            dmap[4] = seq
            pat.remove(seq)

        if len(seq) == 7:
            dmap[8] = seq
            pat.remove(seq)

    for seq in pat.copy():
        if len(seq) == 5:
            if len(set(seq).intersection(set(dmap[7]))) == 3:
                dmap[3] = seq
                pat.remove(seq)

        if len(seq) == 6:
            if len(set(seq).intersection(set(dmap[4]))) == 4:
                dmap[9] = seq
                pat.remove(seq)

    for seq in pat.copy():
        if len(seq) == 5:
            if len(set(seq).intersection(set(dmap[4]))) == 3:
                dmap[5] = seq
                pat.remove(seq)


        if len(seq) == 6:
            if len(set(seq).intersection(set(dmap[7]))) == 3:
                dmap[0] = seq
                pat.remove(seq)

    for seq in pat:
        if len(seq) == 5: dmap[2] = seq
        if len(seq) == 6: dmap[6] = seq

    dmap = dict(zip(dmap.values(),dmap.keys()))

    pat = lines[i].split(' | ')[1].split()
    pat = ["".join(sorted(v)) for v in pat]

    num = ''
    for char in pat:
        num += str(dmap[char])
    nums.append(int(num))

print(sum(nums))