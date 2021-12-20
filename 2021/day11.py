from utils import getFilename, readFile

filename = 'day11.txt'
output = readFile(filename, str, sepChar='\n')
output = [[int(num) for num in o] for o in output]

### PART 1 & 2 ###
class DumboOctopus:
    def __init__(self, row, col, init_val):
        self.val = init_val
        self.flashed = False            # flashed in current step
        self.flash_num = 0              # number of flashes
        self.coords = (row, col)
        self.adj_coords = [(r,c) for (r,c) in [(row-1, col), (row-1, col+1), 
                                               (row, col+1), (row+1, col+1),
                                               (row+1, col), (row+1, col-1),
                                               (row, col-1), (row-1, col-1)]
                            if 0 <= r <= len(output)-1 and 0 <= c <= len(output[0])-1]

    def reset_flashed(self):
        self.flashed = False

    def incr_val(self, octopi):
        self.val += 1
        self.check_flash(octopi)

    def incr_adj(self, octopi):
        for (row, col) in self.adj_coords:
            if not octopi[row][col].flashed:
                octopi[row][col].incr_val(octopi)

    def check_flash(self, octopi):
        if not self.flashed and self.val > 9:
            self.flashed = True
            self.flash_num += 1
            self.val = 0
            self.incr_adj(octopi)

    def __add__(self, other):
        return self.flash_num + other.flash_num

    def __repr__(self):
        return str(self.val)

    def __str__(self):
        return self.val

octopi = [[DumboOctopus(row, col, output[row][col]) for col in range(len(output[row]))] for row in range(len(output))]
# print(octopi)
for step in range(100):
    # 1. increase value of each octopus
    for row in octopi:
        for octopus in row:
            octopus.val += 1
    # 2. propagate flashes
    for row in octopi:
        for octopus in row:
            octopus.check_flash(octopi)
    # 3. reset all octopus to self.flashed = False
    for row in octopi:
        for octopus in row:
            octopus.reset_flashed()

flashes = 0
for row in octopi:
    for octopus in row:
        flashes += octopus.flash_num
print(flashes)


### PART 2 ###
def all_flashed(octopi):
    for row in octopi:
        for octopus in row:
            if not octopus.flashed:
                return False
    return True

octopi = [[DumboOctopus(row, col, output[row][col]) for col in range(len(output[row]))] for row in range(len(output))]
step = 0
while True:
# for step in range(195):
    # 1. increase value of each octopus
    for row in octopi:
        for octopus in row:
            octopus.val += 1
    # 2. propagate flashes
    for row in octopi:
        for octopus in row:
            octopus.check_flash(octopi)

    if all_flashed(octopi):
        print(step+1)
        break

    # 3. reset all octopus to self.flashed = False
    for row in octopi:
        for octopus in row:
            octopus.reset_flashed()

    step += 1