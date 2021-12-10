file = open("p10-input","r")
lines = file.read().splitlines()
file.close()

omap = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}
cmap = dict(zip(omap.values(), omap.keys()))
smap = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

for line in lines.copy():
    f = list()
    for char in list(line):
        if char in omap: # open
            f.append(char)
        if char in cmap:
            if f[len(f) - 1] != cmap[char]:
                print ('Expected ' + omap[f[len(f) -1]] + ', but found ' + char + ' instead.')
                lines.remove(line)
                break
            if f[len(f) - 1] == cmap[char]:
                f.pop(len(f) - 1)

scores = []
for line in lines:
    score = 0
    f = list()
    for char in list(line):
        if char in omap: # open
            f.append(char)
        if char in cmap:
            if f[len(f) - 1] == cmap[char]:
                f.pop(len(f) - 1)

    f.reverse()
    for char in f:
        score = score * 5
        score += smap[omap[char]]

    scores.append(score)

scores.sort()

print(scores[int((len(scores) - 1) * 0.5)])


