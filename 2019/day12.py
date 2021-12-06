import copy

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)

def lcm(a, b):
    return (a * b) // gcd(a,b)

tempText = open("day12.txt", "r").read().split("\n")
text = []
for t in tempText:
    temp = t[:-1].split(", ")
    text.append([int(e[e.index("=")+1:]) for e in temp] + [0,0,0])      # [x, y, z, v_x, v_y, v_z]

text = [[-1, 0, 2, 0, 0, 0], [2, -10, -7, 0, 0, 0], [4, -8, 8, 0, 0, 0], [3, 5, -1, 0, 0, 0]]
# text = [[-1, 0, 2, 0, 0, 0], [2, -10, -7, 0, 0, 0]]
text = [[-8, 10, 0, 0, 0, 0], [5, 5, 10, 0, 0, 0], [2, -7, 3, 0, 0, 0], [9, -8, -3, 0, 0, 0]]
initial = copy.deepcopy(text)

# time = 25
# for t in range(time):
steps = 0
n = 1
repeats = [[0 for i in range(3)] for j in range(len(text))]
while True:
    # if t in [1367, 1368,1369]:
    # print("After", steps, "steps:")
    # for moon in text:
    #     print("pos=", moon[0], moon[1], moon[2], "vel=", moon[3], moon[4], moon[5])

    # add gravity
    for first in range(len(text)):
        for second in range(first+1, len(text)):
            for v in range(3):
                if text[first][v] < text[second][v]:
                    text[first][v+3] += 1
                    text[second][v+3] -= 1
                elif text[first][v] > text[second][v]:
                    text[first][v+3] -= 1
                    text[second][v+3] += 1

    # add velocity
    for moon in text:
        for v in range(3):
            moon[v] += moon[v+3]

    steps += 1
    for m in range(len(text)):
        for x in range(3):
            if repeats[m][x] == 0 and text[m][x] == initial[m][x] and text[m][x+3] == initial[m][x+3]:
                repeats[m][x] = steps
                # print(steps, repeats)
                n = lcm(n,steps)

    if 0 not in sum(repeats, []):
        break

    # if text == initial:
    #     break

    # print()

# PART 1 -- calculate energy (potential * kinetic)
# energies = []
# for moon in text:
#     pot = sum([abs(x) for x in moon[:3]])
#     kin = sum([abs(v) for v in moon[3:]])
#     energies.append(pot * kin)

# print(sum(energies))


# PART 2 -- find step number n when text == initial
# velocities of x and n-x are negative of each other, so sum of x,y,z velocities = 0
# find point where starts to negate?
print(repeats)
print(n, len(str(n)))