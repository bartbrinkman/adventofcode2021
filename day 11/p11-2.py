from pprint import pprint

file = open("p11-input","r")
lines = file.read().splitlines()
file.close()

# small simulation so we can get away with inefficient code

class Octopus:
    instances = set()
    flashes = 0

    def __init__(self, energy, x, y):
        self.energy = int(energy)
        self.x = x
        self.y = y
        Octopus.instances.add(self)

    def step(self):
        self.energy += 1

    def trigger(self):
        if self.energy > 9:
            self.flash()

    def touch(self):
        if self.energy > 0:
            self.energy += 1
        if self.energy > 9:
            self.flash()

    def flash(self):
        self.energy = 0
        Octopus.flashes += 1
        for o in Octopus.instances:
            if o == self: continue

            if self.x - 1 == o.x and self.y - 1 == o.y: o.touch()
            if self.x == o.x     and self.y - 1 == o.y: o.touch()
            if self.x + 1 == o.x and self.y - 1 == o.y: o.touch()

            if self.x - 1 == o.x and self.y == o.y: o.touch()
            if self.x + 1 == o.x and self.y == o.y: o.touch()

            if self.x - 1 == o.x and self.y + 1 == o.y: o.touch()
            if self.x == o.x     and self.y + 1 == o.y: o.touch()
            if self.x + 1 == o.x and self.y + 1 == o.y: o.touch()

    def __repr__(self):
        return str(self.energy)

c = [list(v) for v in lines] # so we can output the field
for y in range(len(c)):
    for x in range(len(c[y])):
        c[y][x] = Octopus(c[y][x], x, y)

for n in range(999):
    for o in Octopus.instances:
        o.step()
    for o in Octopus.instances:
        o.trigger()

    oe = 0
    for o in Octopus.instances:
        oe += o.energy

    if oe == 0:
        pprint(c)
        print('Step ' + str(n + 1))
        exit()

# print(Octopus.flashes)

