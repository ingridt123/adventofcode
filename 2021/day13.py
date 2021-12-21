from utils import getFilename, readFile

filename = 'day13.txt'
output = readFile(filename, str, sepChar='\n')

dot_coords = []
folds = []

coords = True
for o in output:
    if o == '':
        coords = False
    elif coords:
        coords = o.split(',')
        dot_coords.append((int(coords[0]), int(coords[1])))
    else:
        equal_index = o.index('=')
        folds.append((o[equal_index-1], int(o[equal_index+1:])))

### PART 1 ### 
# horizontal (y) folds --> x value stays the same / y value changes to fold_value - abs(y - fold_value)
# vice versa for vertical (x) folds
for fold_dir, fold_val in folds:
    if fold_dir == 'x':
        for i in range(len(dot_coords)):
            dot_coords[i] = (fold_val - abs(dot_coords[i][0] - fold_val), dot_coords[i][1])
    else:
        for i in range(len(dot_coords)):
            dot_coords[i] = (dot_coords[i][0], fold_val - abs(dot_coords[i][1] - fold_val))
    dot_coords = list(set(dot_coords))

print(len(dot_coords))

### PART 2 ###
dot_coords = set(dot_coords)
max_coords = [float('-inf'), float('-inf')]
for x, y in dot_coords:
    if x > max_coords[0]:
        max_coords[0] = x
    if y > max_coords[1]:
        max_coords[1] = y

for y in range(max_coords[1]+1):
    row = []
    for x in range(max_coords[0]+1):
        if (x,y) in dot_coords:
            row.append('#')
        else:
            row.append(' ')
    print("".join(row))