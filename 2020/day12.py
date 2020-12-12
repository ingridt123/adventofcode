import sys
from utils import getFilename, readFile

filename = getFilename(sys.argv)
output = readFile(filename, str)

DIRECTIONS_TURN = ['east', 'south', 'west', 'north']
DIRECTIONS_FORWARD = {'east': [1, 0], 'south': [0, -1], 'west': [-1, 0], 'north': [0, 1]}

output = [(o[0], int(o[1:])) for o in output]


### PART 1 ###

coord = [0,0]
dir_index = 0

for action, value in output:
    if action == 'N':
        coord[1] += value
    elif action == 'S':
        coord[1] -= value
    elif action == 'E':
        coord[0] += value
    elif action == 'W':
        coord[0] -= value
    elif action == 'F':
        direction = DIRECTIONS_TURN[dir_index]
        coord[0] += (DIRECTIONS_FORWARD[direction][0] * value)
        coord[1] += (DIRECTIONS_FORWARD[direction][1] * value)
    elif action == 'L':
        num_turn = value // 90
        dir_index -= num_turn
        if dir_index < 0:
            dir_index = len(DIRECTIONS_TURN) + dir_index
    elif action == 'R':
        num_turn = value // 90
        dir_index = (dir_index + num_turn) % len(DIRECTIONS_TURN)

print(abs(coord[0]) + abs(coord[1]), coord)                          # 2280


### PART 2 ###

waypoint_coord = [10,1]     # relative to ship
coord = [0,0]

for action, value in output:
    if action == 'N':
        waypoint_coord[1] += value
    elif action == 'S':
        waypoint_coord[1] -= value
    elif action == 'E':
        waypoint_coord[0] += value
    elif action == 'W':
        waypoint_coord[0] -= value
    elif action == 'F':
        coord[0] += (waypoint_coord[0] * value)
        coord[1] += (waypoint_coord[1] * value)
    elif action == 'L' or action == 'R':
        num_turn = value // 90
        extra = 0
        if action == 'R':
            extra = 1
        if num_turn % 2 != 0:
            waypoint_coord[0], waypoint_coord[1] = waypoint_coord[1], waypoint_coord[0]
            waypoint_coord[extra] *= -1
        if num_turn // 2 > 0:
            waypoint_coord[0] *= (-1 ** (num_turn // 2))
            waypoint_coord[1] *= (-1 ** (num_turn // 2))

print(abs(coord[0]) + abs(coord[1]), waypoint_coord, coord)            # 38693