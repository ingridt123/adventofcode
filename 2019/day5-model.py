from enum import Enum

# Returns the number at the given position (0 being the rightmost)
def get_nth_digit(n, number):
    return number // 10**n % 10

class Operation(Enum):
    ADDITION = 1
    MULTIPLICATION = 2
    INPUT = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    TERMINATION = 99

class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1

class Instruction:
    def __init__(self, opcode):
        # instruction: 1 is add, 2 is multiply, 3 is input, 4 is output, 99 is end
        self.operation = Operation(get_nth_digit(1, opcode) * 10 + get_nth_digit(0, opcode))
        # mode: 0 is indirect, 1 is immediate
        self.modes = list(map(Mode, [get_nth_digit(2, opcode), get_nth_digit(3, opcode), get_nth_digit(4, opcode)]))

    def __str__(self):
        return "{}, {}".format(repr(self.operation), self.modes)


def opcode_run(ops):
    i = 0
    while ops[i] != 99:
        instruction = Instruction(ops[i])
        print(i, instruction)
        if instruction.operation is Operation.ADDITION:
            first = ops[i+1] if instruction.modes[0] is Mode.IMMEDIATE else ops[ops[i+1]]
            second = ops[i+2] if instruction.modes[1] is Mode.IMMEDIATE else ops[ops[i+2]]
            result = first + second
            # the last mode should *always* be POSITION
            ops[ops[i+3]] = result
            i += 4
            print("1", first, second, ops[i+3])
        elif instruction.operation is Operation.MULTIPLICATION:
            first = ops[i+1] if instruction.modes[0] is Mode.IMMEDIATE else ops[ops[i+1]]
            second = ops[i+2] if instruction.modes[1] is Mode.IMMEDIATE else ops[ops[i+2]]
            val = first * second
            # the last mode should *always* be POSITION
            ops[ops[i+3]] = val
            i += 4
        elif instruction.operation is Operation.INPUT:
            stuff = input("Please enter ID: --> ")
            ops[ops[i+1]] = int(stuff)
            i += 2
        elif instruction.operation is Operation.OUTPUT:
            print (ops[ops[i+1]])
            i += 2
        elif instruction.operation is Operation.JUMP_IF_TRUE:
            first = ops[i+1] if instruction.modes[0] is Mode.IMMEDIATE else ops[ops[i+1]]
            second = ops[i+2] if instruction.modes[1] is Mode.IMMEDIATE else ops[ops[i+2]]
            print("5", first, second)
            if first != 0:
                i = second
            else:
                i += 3
        elif instruction.operation is Operation.JUMP_IF_FALSE:
            first = ops[i+1] if instruction.modes[0] is Mode.IMMEDIATE else ops[ops[i+1]]
            second = ops[i+2] if instruction.modes[1] is Mode.IMMEDIATE else ops[ops[i+2]]
            if first == 0:
                i = second
            else:
                i += 3
            print("6", first, second)
        elif instruction.operation is Operation.LESS_THAN:
            first = ops[i+1] if instruction.modes[0] is Mode.IMMEDIATE else ops[ops[i+1]]
            second = ops[i+2] if instruction.modes[1] is Mode.IMMEDIATE else ops[ops[i+2]]
            ops[ops[i+3]] = 1 if first < second else 0
            i += 4
        elif instruction.operation is Operation.EQUALS:
            first = ops[i+1] if instruction.modes[0] is Mode.IMMEDIATE else ops[ops[i+1]]
            second = ops[i+2] if instruction.modes[1] is Mode.IMMEDIATE else ops[ops[i+2]]
            ops[ops[i+3]] = 1 if first == second else 0
            i += 4
    print ("HALT!")

# Initialize: open file, turn all op codes into integers
with open('day5.txt') as f:
    # split line into operation list
    opsAsStrings = f.read().split(",")
    # turn them all into integers
    ops = list(map(int, opsAsStrings))

# Part One: Enter 1 when prompted and enter number right before HALT!
# Part Two: Enter 5 when prompted and enter number right before HALT!
myOps = ops.copy()
opcode_run(myOps)