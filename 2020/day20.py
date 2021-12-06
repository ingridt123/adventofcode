import sys
from utils import getFilename, readFile
import functools
import operator

filename = getFilename(sys.argv)
output = readFile(filename, str, sepChar='\n')

tiles = dict()

prevTileId = -1
prevTile = []
for o in output:
    if 'Tile' in o:
        if len(prevTile) != 0:
            tiles[prevTileId] = prevTile
            prevTile = []
        prevTileId = int(o[o.index(' ')+1:-1])
    elif o != '':
        prevTile.append(o)
tiles[prevTileId] = prevTile

def getRow(tile, index):
    return tile[index]

def getFirstRow(tile):
    return getRow(tile, 0)

def getLastRow(tile):
    return getRow(tile, len(tile)-1)

def getCol(tile, index):
    col = []
    for row in tile:
        col.append(row[index])
    return col

def getFirstCol(tile):
    return getCol(tile, 0)

def getLastCol(tile):
    return getCol(tile, len(tile[0])-1)

def getMatchDict(tiles):
    matchDict = dict()
    for t in tiles:
        tile = tiles[t]
        edges = [tuple(getFirstRow(tile)), tuple(getLastCol(tile)), 
                 tuple(getLastRow(tile)), tuple(getFirstCol(tile))]

        for i in range(len(edges)):
            if edges[i] in matchDict:
                matchDict[edges[i]][i] = t
            else:
                newMatch = [-1 for x in range(4)]
                newMatch[i] = t
                matchDict[edges[i]] = newMatch

    return matchDict


def findMatches(matchDict):
    # brute force: check all possible pairs
    # or dictionary tuple of row/column -> [list of tileIds that match -- top, right, bottom, left]
    matches = dict()
    for m in matchDict:
        matchDict[m] = [x for x in matchDict[m] if x != -1]
        if len(matchDict[m]) == 2:
            if matchDict[m][0] not in matches:
                matches[matchDict[m][0]] = [matchDict[m][1]]
            else:
                matches[matchDict[m][0]].append(matchDict[m][1])
            
            if matchDict[m][1] not in matches:
                matches[matchDict[m][1]] = [matchDict[m][0]]
            else:
                matches[matchDict[m][1]].append(matchDict[m][0])

    return matches

def findCorners(matches):
    corners = []
    for m in matches:
        if len(matches[m]) == 2:
            corners.append(m)

    return corners


### DAY 1 ###
# to find four corner tiles, find four tiles such that two edges don't match with any other
# top-left: top and left
# top-right: top and right
# bottom-left: bottom and left
# bottom-right: bottom and right

# matches = dict()        # tileId -> [list of tileIds that match -- top, right, bottom, left]

# for t in tiles:
#     matches[t] = [-1 for i in range(4)]

# for t in tiles:
#     print(t, tiles[t])
# matchDict = getMatchDict(tiles)
# # print(matchDict)
# for m in matchDict:
#     print(m, matchDict[m])
# matches = findMatches(matchDict)
# corners = findCorners(matches)
# print(corners)
# print(functools.reduce(operator.mul, corners, 1))

print(getLastCol(['####...##.', '#..##.#..#', '##.#..#.#.', '.###.####.', '..###.####', '.##....##.', '.#...####.', '#.##.####.', '####..#...', '.....##...']))