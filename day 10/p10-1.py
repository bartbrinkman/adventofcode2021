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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

score = 0
for n in range(len(lines)):
    f = list()
    for char in list(lines[n]):
        if char in omap: # open
            f.append(char)
        if char in cmap:
            if f[len(f) - 1] != cmap[char]:
                print ('Expected ' + omap[f[len(f) -1]] + ', but found ' + char + ' instead.')
                score += smap[char]
                break
            if f[len(f) - 1] == cmap[char]:
                f.pop(len(f) - 1)

print(score)


