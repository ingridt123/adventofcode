def main():
    text = open("day3.txt", "r").read().split()
    # text = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
    # text = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
    # text = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
    instruct1 = text[0].split(",")
    instruct2 = text[1].split(",")
    
    path1 = wirePath(instruct1)
    path2 = wirePath(instruct2)
    # print(path1)
    # print(path2)

    intersections = [p for p in path1 if p in path2]
    distance = [path1.index(i) + path2.index(i) + 2 for i in intersections]
    # intersections = [(abs(x),abs(y)) for (x,y) in path1 if (x,y) in path2]
    # print(intersections)
    # print(min(list(map(sum, intersections))))
    print(min(distance))


def wirePath(instruct):
    curRow = 0
    curCol = 0

    path = []

    for i in instruct:
        direct = i[0]
        dist = int(i[1:])
        print(i)
        if direct == "U":
            path += [(row, curCol) for row in range(curRow+1, curRow+dist+1) if (row, curCol) not in path]
            curRow = curRow+dist
        elif direct == "D":
            path += [(row, curCol) for row in range(curRow-1, curRow-dist-1, -1) if (row, curCol) not in path]
            curRow = curRow-dist
        elif direct == "R":
            path += [(curRow, col) for col in range(curCol+1, curCol+dist+1) if (curRow, col) not in path]
            curCol = curCol+dist
        elif direct == "L":
            path += [(curRow, col) for col in range(curCol-1, curCol-dist-1, -1) if (curRow, col) not in path]
            curCol = curCol-dist

    return path

main()

# print(intersections)
# print(max(list(map(sum, intersections))))