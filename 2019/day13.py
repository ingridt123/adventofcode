import intcode

text = intcode.readFile("day13.txt")

# 0 = empty tile
# 1 = wall tile (indestructible)
# 2 = block tile (destructible)
# 3 = horizontal paddle (indestructible)
# 4 = ball

# memory position 0 = number of quarters inserted
text[0] = 2

# x y tile_id
output = intcode.compute(text)

screen = []
for i in range(0,len(output),3):
    if output[i+2] == 2 and (output[i], output[i+1]) not in screen:
        screen.append((output[i], output[i+1]))

print(len(screen))