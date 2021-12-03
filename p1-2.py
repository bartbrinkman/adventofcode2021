import urllib.request

def array_index_exists(array, index):
    return 0 <= index < len(array)

file = open("p1-input","r")
lines = file.read().splitlines()
file.close()

prev = 0
num = 0

for index, line in enumerate(lines):
    if array_index_exists(lines, index - 1) and array_index_exists(lines, index) and array_index_exists(lines, index + 1):
        avg = (int(lines[index - 1]) + int(lines[index]) + int(lines[index + 1])) / 3 # or: sum(lines[index:index+3])
        if avg > prev:
            num += 1

        prev = avg

print(num - 1)

