import urllib.request

file = open("p1-input","r")
lines = file.read().splitlines()
file.close()

prev = 0
num = 0

for line in lines:
    line = int(line)
    if line > prev:
        num += 1

    prev = line

print(num - 1)


