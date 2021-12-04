import re
from pprint import pprint
from copy import deepcopy

def calc_score(board, num):
    board = deepcopy(board)
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == -1: board[r][c] = 0
        board[r] = sum(board[r])

    return sum(board) * num

def scan_rows(boards, num):
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            if sum(boards[b][r]) == -5:
                score = calc_score(boards[b], num)
                print(num, score)
                pprint(boards[b])
                boards.pop(b)
                return scan_rows(boards, num)

def scan_columns(boards, num):
    for b in range(len(boards)):
        for i in range(len(boards[0])):
            c = []
            for r in range(len(boards[b])):
                c.append(boards[b][r][i])
            if sum(c) == -5:
                score = calc_score(boards[b], num)
                print(num, score)
                pprint(boards[b])
                boards.pop(b)
                return scan_columns(boards, num)

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

for num in seq:
    for b in range(len(boards)):
        for r in range(len(boards[b])):
            for c in range(len(boards[b][r])):
                if num == boards[b][r][c]: boards[b][r][c] = -1

    scan_rows(boards, num)
    scan_columns(boards, num)
