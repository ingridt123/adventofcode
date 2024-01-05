from functools import reduce
from enum import Enum
import pydot
import re
from utils import read_file

class ModuleType(Enum):
  FLIP_FLOP = '%'
  CONJUNCTION = '&'
  THROUGH = ''

class PulseType(Enum):
  Low = 'low'
  High = 'high'

class Module:
  def __init__(self, s):
    match = re.match(r'([\%|\&]*)(\w+) -> ([\w\, ]+)', s)
    if match[1] == '%':
      self.type = ModuleType.FLIP_FLOP
      self.dotType = '\\' + self.type.value
      self.off = True
    elif match[1] == '&':
      self.type = ModuleType.CONJUNCTION
      self.dotType = self.type.value
      self.prevModOutputs = dict()
    else:
      self.type = ModuleType.THROUGH
      self.dotType = self.type.value

    self.name = match[2]
    self.nextMods = re.split(r'\, ', match[3])

  def __repr__(self):
    return f"{self.name} ({self.type}) -> {self.nextMods}"

def parseInput(strs):
  modules = dict()
  modules['button'] = Module('button -> broadcaster')
  for s in strs:
    m = Module(s)
    modules[m.name] = m

  # set prevModOutputs for conjunction modules
  for m in modules:
    for n in modules[m].nextMods:
      if n in modules and hasattr(modules[n], 'prevModOutputs'):
        modules[n].prevModOutputs[m] = PulseType.Low

  return modules

def pressButtonOnce(modules, xx=None):
  queue = [('button', 'broadcaster', PulseType.Low)]
  history = [('button', 'broadcaster', PulseType.Low)]
  numLows = 0
  numHighs = 0

  lowPulseToXX = False

  while len(queue) > 0:
    src, dest, pulse = queue.pop(0)
    if pulse == PulseType.Low:
      numLows += 1
    else:
      numHighs += 1

    if xx is not None and dest == xx and pulse == PulseType.Low:
      lowPulseToXX = True

    if dest not in modules:
      continue
    module = modules[dest]

    if module.type == ModuleType.THROUGH:
      for nextMod in module.nextMods:
        queue.append((module.name, nextMod, pulse))
        history.append((module.name, nextMod, pulse))

    elif module.type == ModuleType.FLIP_FLOP:
      if pulse == PulseType.Low:
        outputPulse = PulseType.High if module.off else PulseType.Low
        module.off = not module.off
        for nextMod in module.nextMods:
          queue.append((module.name, nextMod, outputPulse))
          history.append((module.name, nextMod, outputPulse))

    elif module.type == ModuleType.CONJUNCTION:
      module.prevModOutputs[src] = pulse
      outputPulse = PulseType.Low if all(p == PulseType.High for p in module.prevModOutputs.values()) else PulseType.High
      for nextMod in module.nextMods:
        queue.append((module.name, nextMod, outputPulse))
        history.append((module.name, nextMod, outputPulse))
        
  return modules, history, numLows, numHighs, lowPulseToXX

def printHistory(history):
  for h in history:
    print(f"{h[0]} -{h[2].value}-> {h[1]}")

#### PART 1 ####
def lookForCycle1(modules):
  # fullHistory = []
  # fullHistoryPulses = []
  numLowsTotal = 0
  numHighsTotal = 0
  # history = []
  # while len(fullHistory) <= 1 or fullHistory[0] != history:
  for _ in range(1000):
    modules, _, numLows, numHighs, _ = pressButtonOnce(modules)
    numLowsTotal += numLows
    numHighsTotal += numHighs
    # fullHistory.append(history)
    # fullHistoryPulses.append((numLows, numHighs))
    # printHistory(history)
    # print()
  
  return numLowsTotal, numHighsTotal

strs = read_file('day20.txt')
step1 = parseInput(strs)
step2_1, step2_2 = lookForCycle1(step1)
print(step2_1 * step2_2)

#### PART 2 ####
def lookForCycle2(modules, xx):
  pressNum = 1
  lowPulseToXX = False
  period = []
  while True:
    modules, _, _, _, lowPulseToXX = pressButtonOnce(modules, xx)
    if lowPulseToXX:
      period.append(pressNum)
      if len(period) == 10:
        break
    if pressNum % 10000 == 0:
      print(f'...Button has been pressed {pressNum} times for {xx}...')
    pressNum += 1
  
  # check if it is cyclic
  cyclic = period == [period[0] * i for i in range(1,11)]
  if cyclic:
    return period[0]
  return None

def graphModules(modules):
  graph = pydot.Dot('modules', graph_type='graph')
  for m in modules:
    graph.add_node(pydot.Node(f'{modules[m].dotType}{m}'))
  graph.add_node(pydot.Node('rx', color='red'))
  for m in modules:
    for n in modules[m].nextMods:
      nextModType = '' if n not in modules else modules[n].dotType
      graph.add_edge(pydot.Edge(f'{modules[m].dotType}{m}', f'{nextModType}{n}', dir='forward'))
  graph.write_png('day20.png')
  print('Graph of modules saved to day20.png')

strs = read_file('day20.txt')
# graphModules(step1)
step2 = []
for xx in ['fh', 'lk', 'hh', 'fn']:
  step1 = parseInput(strs)
  step2.append(lookForCycle2(step1, xx))
step3 = reduce(lambda a,b: a*b, step2)  # lcm since all in step2 are prime
print(step3)

# The following must all be high for &nc -> rx to be low:
# &fh -> &nc
# &lk -> &nc
# &hh -> &nc
# &fn -> &nc
# 
# So the following must all be low:
# &gl -> &fh 3851
# &gk -> &lk 4003
# &hr -> &hh 4027
# &nr -> &fn 3847
# which means not all inputs to these sources are high
#
# So if each of these subgraphs are cyclic, then the LCM of their periods is when &nc -> rx is low