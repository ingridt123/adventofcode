# from collections import defaultdict
# import copy
# import re
# from utils import read_file

# def parseInput(s):
#   match = re.match(r'([\%|\&]*)(\w+) -> ([\w\, ]+)', s)
#   modType = match[1]
#   modName = match[2]
#   modDest = re.split(r'\, ', match[3])
#   return modType, modName, modDest

# def getModuleReverseMapping(modules):
#   mappings = defaultdict(list)
#   mappings['broadcaster'] = ['button']
#   for m in modules:
#     for dest in m[2]:
#       mappings[dest].append(m[1])
#   return mappings

# def getModulesDict(modules):
#   modulesDict = dict()
#   for m in modules:
#     modulesDict[m[1]] = m
#   return modulesDict

# def pressButtonOnce(currentState, modules):
#   reverseMappings = getModuleReverseMapping(modules)
#   modulesDict = getModulesDict(modules)
#   history = [(False, 'button', 'broadcaster')]
#   queue = [(False, 'broadcaster', m[1]) for m in modules if m[0] == 'broadcaster']
#   count = 0
#   while len(queue) > 0:
#     count += 1
#     if count > 5:
#       break
#     print(queue)
#     pulseMod = queue.pop(0)
#     pulse = pulseMod[0]
#     pulseSrc = pulseMod[1]
#     modName = pulseMod[2]
#     if modName not in modulesDict:
#       continue
#     m = modulesDict[modName]
#     modType = m[0]
#     modDest = m[2]

#     if modType == '':         # pass on input to output
#       for dest in modDest:
#         currentState[(modName, dest)] = pulse
#         history.append((currentState[(modName, dest)], modName, dest))
#         queue.append((currentState[(modName, dest)], modName, dest))
#     elif modType == '%':      # flip flop (when L received, flips output // ignores H)
#       print(currentState[(reverseMappings[modName][0], modName)], reverseMappings[modName][0])
#       if currentState[(reverseMappings[modName][0], modName)] == False:
#         for dest in modDest:
#           currentState[(modName, dest)] = not currentState[(modName, dest)]
#           history.append((currentState[(modName, dest)], modName, dest))
#           queue.append((currentState[(modName, dest)], modName, dest))
#     else:                     # conjunction (if H for all inputs in memory, outputs L, else H)
#       allHigh = all([currentState[(src, modName)] for src in reverseMappings[modName]])
#       for dest in modDest:
#         currentState[(modName, dest)] = not allHigh
#         history.append((currentState[(modName, dest)], modName, dest))
#         queue.append((currentState[(modName, dest)], modName, dest))
#   return currentState, history

# def getInitialState(modules):
#   state = dict()
#   state[('button', 'broadcaster')] = False
#   for m in modules:
#     for dest in m[2]:
#       state[(m[1], dest)] = False
#   return state

# def isCurrentStateRepeat(currentState, prevCurrentStates):
#   for s in prevCurrentStates[:-1]:
#     if s == currentState:
#       return True
#   return False

# def findCycle(modules):
#   currentState = getInitialState(modules)
#   prevCurrentStates = [copy.deepcopy(currentState)]
#   print(currentState)
#   history = []
#   count = 1
#   while not isCurrentStateRepeat(currentState, prevCurrentStates):
#     currentState, newHistory = pressButtonOnce(currentState, modules)
#     prevCurrentStates.append(copy.deepcopy(currentState))
#     print(count)
#     print(currentState)
#     for h in newHistory:
#       print(f'{h[1]} -{"high" if h[0] else "low"}-> {h[2]}')
#     # print(newHistory)
#     print()
#     history.append(newHistory)
#     count += 1
#   return history

# def calculateNumPulses(history):
#   numLow = 0
#   numHigh = 0
#   for i in range(len(history)-1):
#     print(history[i])
#     numRepeat = 1000 // (len(history)-1)
#     if i < 1000 % (len(history)-1):
#       numRepeat += 1
#     pulses = [h[0] for h in history[i]]
#     numLow += (pulses.count(False) * numRepeat)
#     numHigh += (pulses.count(True) * numRepeat)
#   print(numLow, numHigh)
#   return numLow * numHigh

# #### PART 1 ####
# strs = read_file('day20-test1.txt')
# step1 = list(map(parseInput, strs))
# # print(step1)
# step2 = findCycle(step1)
# # print(step2)
# step3 = calculateNumPulses(step2)
# print(step3)