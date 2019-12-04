text = open("day2.txt", "r").read().split(",")
text = [int(t) for t in text]

# text[1] = 12
# text[2] = 2
# text = [2,3,0,3,99]
store = text.copy()
# print(text, store)

for noun in range(0,100):
    for verb in range(0,100):
        text = store.copy()
        text[1] = noun
        text[2] = verb
        for i in range(0, len(text), 4):
            if text[i] == 99:
                break
            elif len(text) > i+3 and len(text) > text[i+3]:
                if text[i] == 1:      # add
                    text[text[i+3]] = text[text[i+1]] + text[text[i+2]]
                elif text[i] == 2:      # multiply
                    text[text[i+3]] = text[text[i+1]] * text[text[i+2]]
        if text[0] == 19690720:
            print(100 * noun + verb)
            break
    

# print(text)