import re
from pprint import pprint

def calc_score(board, num):

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == -1: board[r][c] = 0
        board[r] = sum(board[r])
    score = sum(board) * num

    pprint(score)

    exit()


file = open("p4-input","r")
lines = file.read().splitlines()
file.close()

seq = lines.pop(0).split(',')
seq = [int(num) for num in seq]
lines.pop(0)

boards = []
board = []
for line in lines:
    if line == '':
        boards.append(board)
        board = []
        continue

    r = re.split('\s+', line.strip())
    board.append([int(c) for c in r])

# replace the number from a board with -1
# check the board for an empty row (sum = -5)
# check the board for an empty column (sum of every column by index is -5)

for num in seq:
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c in range(len(boards[b][r])):
                if num == boards[b][r][c]: boards[b][r][c] = -1

    for b in range(len(boards)):
        for r in range(len(boards[b])):
            if sum(boards[b][r]) == -5:
                calc_score(boards[b], num)

    for b in range(len(boards)):
        for i in range(len(boards[0])):
            c = []
            for r in range(len(boards[b])):
                c.append(boards[b][r][i])
            if sum(c) == -5:
                calc_score(boards[b], num)

