from utils import getFilename, readFile
from functools import reduce

filename = 'day9.txt'
output = readFile(filename, str, sepChar='\n')
output = [[int(num) for num in o] for o in output]

### PART 1 ###
risk = 0
low_points = []
for row in range(len(output)):
    for col in range(len(output[row])):
        val = output[row][col]
        if row != 0 and output[row-1][col] <= val:                      # up
            continue
        if row != len(output)-1 and output[row+1][col] <= val:          # down
            continue
        if col != 0 and output[row][col-1] <= val:                      # left
            continue

        if col != len(output[row])-1 and output[row][col+1] <= val:     # right
            continue

        low_points.append((row, col))
        risk += val + 1
print(risk)

### PART 2 ###
def find_basin(row, col, low_points, output):
    # path.add((row, col))
    if (row, col) in low_points:
        return (row, col)
    # TODO: optimize further by adding all the coordinates on the path to the basin instead of checking each individual one
    # TODO: check coordinates on the path for matches, don't have to go all the way down to the low_point
    # elif (row, col) in visited:
    #     for low_point in basins:
    #         if (row, col) in basins[low_point]:
    #             return low_point
    
    adj_coords = [(output[r][c], r,c) for (r,c) in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
                    if 0 <= r <= len(output)-1 and 0 <= c <= len(output[row])-1 and output[r][c] < output[row][col]]

    _, max_r, max_c = max(adj_coords)
    return find_basin(max_r, max_c, basins, output)

basins = dict()
for point in low_points:
    basins[point] = set()

for row in range(len(output)):
    for col in range(len(output[row])):
        if (row, col) not in low_points and output[row][col] != 9:
            end_point = find_basin(row, col, low_points, output)
            basins[end_point].add((row, col))

sizes = list(map(lambda x: len(x)+1, basins.values()))
print(sizes)
print(reduce(lambda a,b: a * b, sorted(sizes, reverse=True)[:3]))