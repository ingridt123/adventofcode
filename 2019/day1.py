import math

text = open("day1.txt", "r").read().split()
# text = ["100756"]

sum = 0
for t in text:
    temp = int(t)
    while temp > 0:
        temp = math.floor(temp/3)-2
        if temp > 0:
            sum += temp

print(sum)