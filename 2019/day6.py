text = open("day6.txt", "r").read().split()

planets = []

for t in text:
    a,b = t.split(")")
    allPlanets = sum(planets, [])
    print(a,b)

    # if both planets not in list, add "A)B" as ["A", "B"]
    if a not in allPlanets and b not in allPlanets:
        planets.append([a,b])

    elif a in allPlanets:
        copy = planets[:]
        for p in copy:
            # if first planet at end, add second planet to end
            if p[-1] is a:
                p.append(b)
            # if first planet in middle, create new list with all before, add second planet to end
            elif a in p:
                # print(p[:p.index(a)+1] + list(b))
                planets.append(p[:p.index(a)+1] + [b,])

    elif b in allPlanets:
        copy = planets[:]
        for p in copy:
            # if second planet at start, add first planet to start (for all)
            if p[0] is b:
                p.insert(0, a)
            # if second planet in middle, create new list with all after, add first planet to start
            elif b in p:
                planets.append([a,] + p[p.index(b):])

    # combine -- if any first and last character the same
    copy = planets[:]
    # print(copy)
    for p in copy:
        matches = [x for x in copy if x[0] == p[-1]]
        if matches:
            for m in matches:
                planets.append(p + m[1:])
                if m in planets: planets.remove(m)
            planets.remove(p)

    # print(t, planets)

# for t in text:
#     a,b = t.split(")")
#     print(a,b)
#     allPlanets = sum(planets, [])

#     # check if first planet already in array
#     # if no, add both to new array
#     if (a not in allPlanets) and (b not in allPlanets):
#         planets.append([a,b])
#         # print("add", planets)

#     # if first planet in array
#     if a in allPlanets:
#         indexes = []
#         for i in range(len(planets)):
#             if a in planets[i]:
#                 indexes.append(i)
#         # indexes = [i in i for range(len(planets)) if a in planets[i]]

#         # check if any planet afterwards in array
#         # if no, append to end of array
#         # if yes, create new array with all planets before + new planet
#         for i in indexes:
#             if planets[i][-1] == a:
#                 planets[i].append(b)
#             else:
#                 index = planets[i].index(a)
#                 planets.append(planets[i][:index+1] + [b])

#     # if second planet in array
#     if b in allPlanets:
#         indexes = []
#         for i in range(len(planets)):
#             if b in planets[i]:
#                 indexes.append(i)

#     # check if any planet before in array
#         for i in indexes:
#             if planets[i][0] == b:
#                 planets[i].insert(0, a)
#             else:
#                 index = planets[i].index(b)
#                 planets.append(planets[i][:index] + [a, b])

#     for p1 in planets:
#         for p2 in planets:

#     print(planets)

# count number of orbits
counted = []
count = 0
for p in planets:
    for i in p:
        if i not in counted:
            count += p.index(i)
            counted.append(i)

print(counted)
print(count)
    

# if both planets not in list, add "A)B" as ["A", "B"]
# if first planet at end, add second planet to end
# if first planet in middle, create new list with all before, add second planet to end
# if second planet at start, add first planet to start (for all)