import sys
from utils import getFilename, readFile

filename = getFilename(sys.argv)
output = readFile(filename, str)

CYCLES = 6


def getCurrentCoords(config):
    coords = set()
    for c in config:
        coords.add(c)

    return coords


def checkCube(coord, config, dimension):
    if dimension == 3:
        coords = getNeighborCoords_3d(coord)
    elif dimension == 4:
        coords = getNeighborCoords_4d(coord)
    active = 0
    for c in coords:
        if c in config and config[c] == '#':
            active += 1
        if active > 3:
            break

    if coord in config and config[coord] == '#':
        if not 2 <= active <= 3:
            return '.'
        return '#'
    else:
        if active == 3:
            return '#'
        return '.'


### PART 1 ###

config = dict()

for y in range(len(output)):
    for x in range(len(output[y])):
        config[(x,y,0)] = output[y][x]

def getNeighborCoords_3d(coord):
    xCoord = coord[0]
    yCoord = coord[1]
    zCoord = coord[2]
    coords = set()
    for x in range(xCoord-1, xCoord+2):
        for y in range(yCoord-1, yCoord+2):
            for z in range(zCoord-1, zCoord+2):
                if x != xCoord or y != yCoord or z != zCoord:
                    coords.add((x,y,z))

    return coords



# check all cubes that are neighbors of one or more existing cubes
for cycle in range(CYCLES):
    allCoords = set()
    for c in config:
        coords = getNeighborCoords_3d(c)
        allCoords = allCoords | coords

    allCoords = allCoords | getCurrentCoords(config)

    newConfig = dict()
    for coord in allCoords:
        newConfig[coord] = checkCube(coord, config, 3)

    config = newConfig

print(list(config.values()).count('#'))                 # 386


### PART 2 ###

config = dict()

for y in range(len(output)):
    for x in range(len(output[y])):
        config[(x,y,0, 0)] = output[y][x]


def getNeighborCoords_4d(coord):
    xCoord = coord[0]
    yCoord = coord[1]
    zCoord = coord[2]
    wCoord = coord[3]
    coords = set()
    for x in range(xCoord-1, xCoord+2):
        for y in range(yCoord-1, yCoord+2):
            for z in range(zCoord-1, zCoord+2):
                for w in range(wCoord-1, wCoord+2):
                    if x != xCoord or y != yCoord or z != zCoord or w != wCoord:
                        coords.add((x,y,z, w))

    return coords


# check all cubes that are neighbors of one or more existing cubes
for cycle in range(CYCLES):
    allCoords = set()
    for c in config:
        coords = getNeighborCoords_4d(c)
        allCoords = allCoords | coords

    allCoords = allCoords | getCurrentCoords(config)

    newConfig = dict()
    for coord in allCoords:
        newConfig[coord] = checkCube(coord, config, 4)

    config = newConfig

print(list(config.values()).count('#'))                 # 386