from utils import readFile

output = readFile("day7.txt", str, sepChar="\n")
# output = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
#           'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
#           'bright white bags contain 1 shiny gold bag.',
#           'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
#           'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
#           'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
#           'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
#           'faded blue bags contain no other bags.',
#           'dotted black bags contain no other bags.']
# output = ['light red bags contain 1 bright white bag, 2 muted yellow bags.',
#           'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
#           'bright white bags contain 1 shiny gold bag.',
#           'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
#           'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
#           'dark olive bags contain no other bags.',
#           'vibrant plum bags contain no other bags.',
#           'faded blue bags contain no other bags.',
#           'dotted black bags contain no other bags.']

# populate bags dictionary (color -> {color -> num})
bags = dict()
for o in output:
    bagColor = o[:o.index(" bags")]
    rest = o[o.index("contain")+8:]
    bagsInside = dict()
    while len(rest) > 0:
        try:
            num = int(rest[:rest.index(" ")])
            rest = rest[rest.index(" ")+1:]
            color = rest[:rest.index(" bag")]
            bagsInside[color] = num
            rest = rest[rest.index(", ")+2:]
        except ValueError:
            break
    
    bags[bagColor] = bagsInside

### PART 1 ###

# store colors to find in queue
colors = ['shiny gold']
allColors = set()
while len(colors) != 0:
    for b in bags:
        if colors[0] in bags[b]:
            allColors.add(b)
            colors.append(b)
    colors.pop(0)

print(len(allColors))


### PART 2 ###

def countBags(bags, color):
    if len(bags[color]) == 0:
        return 1

    total = 1
    for b in bags[color]:
        total += (bags[color][b] * countBags(bags, b))

    return total


# subtract 1 because count includes shiny gold bag
print(countBags(bags, 'shiny gold')-1)