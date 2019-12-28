import intcode

text = intcode.readFile("day9.txt")
# text = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# text = [1102,34915192,34915192,7,4,7,99,0]
# text = [104,1125899906842624,99]

intcode.compute(text)

# def intcode(text):
#     # inputIndex = 0
#     relBase = 0

#     i = 0
#     while i < len(text):
#         # get values from current position
#         opcode = text[i] % 100
#         modes = []
#         vals = []
#         params = text[i] // 100
#         paramNum = 0

#         # set paramNum and parameters based on opcode
#         if opcode in [1,2,7,8]:
#             paramNum = 3
#         elif opcode in [3,4,9]:
#             paramNum = 1
#         elif opcode in [5,6]:
#             paramNum = 2
#         for p in range(paramNum):
#             modes.append(params % 10)
#             if modes[p] == posMode:
#                 text = checkIndex(i+p+1, text)
#                 text = checkIndex(text[i+p+1], text)
#                 vals.append(text[text[i+p+1]])
#             elif modes[p] == imMode:
#                 vals.append(text[i+p+1])
#             elif modes[p] == relMode:
#                 text = checkIndex(i+p+1, text)
#                 text = checkIndex(relBase+text[i+p+1], text)
#                 vals.append(text[relBase + text[i+p+1]])
#             params = params // 10
#         print(i, opcode, modes, vals)

#         # perform operation based on opcode
#         if opcode == 1:         # add
#             text = checkIndex(text[i+3], text)
#             text[text[i+3]] = vals[0] + vals[1]
#             print(text[i+3], text[text[i+3]])
#             i += 4
#         elif opcode == 2:      # multiply
#             text = checkIndex(text[i+3], text)
#             text[text[i+3]] = vals[0] * vals[1]
#             print(text[i+3], text[text[i+3]])
#             i += 4
#         elif opcode == 3:      # stores input
#             text = checkIndex(vals[0], text)
#             text[vals[0]] = int(input("Enter ID: "))
#             print(relBase, i+1, text[i+i], vals[0], text[vals[0]])
#             # inputIndex += 1
#             i += 2
#         elif opcode == 4:      # outputs
#             print(vals[0])
#             # return text[text[i+1]]
#             i += 2
#         elif opcode == 5:       # jump if true
#             if vals[0] != 0:
#                 i = vals[1]
#             else:
#                 i += 3
#             print(i, text[i])
#         elif opcode == 6:       # jump if false
#             if vals[0] == 0:
#                 i = vals[1]
#             else:
#                 i += 3
#         elif opcode == 7:       # less than
#             text = checkIndex(text[i+3], text)
#             if vals[0] < vals[1]:
#                 text[text[i+3]] = 1
#             else:
#                 text[text[i+3]] = 0
#             print(text[i+3], text[text[i+3]])
#             i += 4
#         elif opcode == 8:       # equals
#             text = checkIndex(text[i+3], text)
#             if vals[0] == vals[1]:
#                 text[text[i+3]] = 1
#             else:
#                 text[text[i+3]] = 0
#             print(text[i+3], text[text[i+3]])
#             i += 4
#         elif opcode == 9:       # adjust relBase
#             relBase += vals[0]
#             print(i+1, text[i+1], relBase)
#             i += 2
#         elif opcode == 99:
#             print("HALT")
#             break
#         else:
#             print("INVALID")
#             break
#         print("text[26]", text[26])
#         if len(text) > 1000:
#             print("text[1000]", text[1000])
#     # print("HALT without opcode 99")

# def checkIndex(index, text):
#     if index >= 0 and index >= len(text):
#         text += [0 for i in range(index - len(text) + 1)]
#     return text
