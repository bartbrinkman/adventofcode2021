import re

file = open("p13-input","r")
lines = file.read().splitlines()
file.close()

def get_max(paper):
    x = []
    y = []
    for c in paper:
        x.append(c[0])
        y.append(c[1])

    return [max(x), max(y)]

def show_paper(paper):
    m = get_max(paper)
    for y in range(m[1] + 1):
        for x in range(m[0] + 1):
            dot = False
            if [x, y] in paper:
                dot = True

            if dot == True: print('█', end='')
            if dot == False: print(' ', end='')

        print("")

def show_dots(paper):
    p = [str(v[0]) + ',' + str(v[1]) for v in paper.copy()]
    print(len(set(p)))


paper = []
instructions = []

for line in lines:
    matched = re.match('(\d+),(\d+)', line)
    if matched:
        paper.append([int(matched[1]), int(matched[2])])

    matched = re.match('fold along ([xy])=(\d+)', line)
    if matched:
        instructions.append([matched[1], int(matched[2])])

for fold in instructions:
    d = 0
    if fold[0] == 'y':
        d = 1

    m = get_max(paper)
    for i in range(len(paper)):
        if paper[i][d] > fold[1]:
            paper[i][d] = (fold[1] - (paper[i][d] - fold[1]))

show_paper(paper)