from utils import getFilename, readFile

filename = 'day10.txt'
output = readFile(filename, str, sepChar='\n')

OPEN_CLOSE = {'(': ')', '[': ']', '{': '}', '<': '>'}
PART1_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
PART2_SCORES = {'(': 1, '[': 2, '{': 3, '<': 4}

### PART 1 & 2 ###
part1_score = 0
part2_scores = []
for o in output:
    corrupt = False
    open = []
    # if open, append to list, otherwise check if it matches last in list
    for c in o:
        if c in OPEN_CLOSE.keys():
            open.append(c)
        elif c == OPEN_CLOSE[open[-1]]:
            open.pop()
        else:
            part1_score += PART1_SCORES[c]
            corrupt = True
            break
    if not corrupt and len(open) != 0:
        part2_score = 0
        for remaining in open[::-1]:
            part2_score *= 5
            part2_score += PART2_SCORES[remaining]
        part2_scores.append(part2_score)

print(part1_score)
print(len(part2_scores))
print(sorted(part2_scores)[len(part2_scores)//2])