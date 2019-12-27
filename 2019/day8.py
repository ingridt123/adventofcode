text = int(open("day8.txt", "r").read())
# text = 222112222120000
# text = 123456789012

width = 25
height = 6
# width = 2
# height = 2
divisor = 10 ** (width * height)

layers = []
while text > 0:
    layer = list(str(text % divisor))
    layer = [int(l) for l in layer]
    layers.append(layer)
    text //= divisor
layers.reverse()
# layers[0].insert(0, 0)
# layers[-1] = [0, 0, 0, 0]

# PART 1
numOfZeros = []
for l in layers:
    numOfZeros.append(l.count(0))

minIndex = numOfZeros.index(min(numOfZeros))

ones = layers[minIndex].count(1)
twos = layers[minIndex].count(2)
print(ones * twos)

# PART 2
for row in range(height):
    for col in range(width):
        for l in layers:
            pixel = l[row*width + col]
            # 0 = black
            # 1 = white
            # 2 = transparent
            if pixel != 2:
                if pixel == 1:
                    print(" ", end="")
                else:
                    print(pixel, end="")
                break
    print()

# YGRYZ