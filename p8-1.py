import re

file = open("p8-input","r")
lines = file.read().splitlines()
file.close()

num = []
for line in lines:
    digits = line.split(' | ')[1].split()
    for digit in digits:
        if len(digit) == 2: num.append(digit)
        if len(digit) == 3: num.append(digit)
        if len(digit) == 4: num.append(digit)
        if len(digit) == 7: num.append(digit)

print(len(num))