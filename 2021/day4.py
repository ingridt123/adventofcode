from utils import getFilename, readFile

filename = 'day4.txt'
output = readFile(filename, '')

nums = [int(o) for o in output[0].split(',')]
cards = [[output[i:i+5], output[i+5:i+10], output[i+10:i+15], output[i+15:i+20], output[i+20:i+25]] for i in range(1, len(output)-24, 25)]

NUM_ROWS = 5
NUM_COLS = 5

def markNum(card, num):
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            if card[i][j] != 'x' and int(card[i][j]) == num:
                card[i][j] = 'x'
                return card
    return card

def markNumAllCards(cards, num):
    return [markNum(card, num) for card in cards]

def checkCard(card):
    if any([row == ['x'] * NUM_COLS for row in card]):
        return True
    cols = [[card[i][j] for i in range(NUM_ROWS)] for j in range(NUM_COLS)]
    return any(col == ['x'] * NUM_ROWS for col in cols)

def checkForWin(cards):
    check = [checkCard(card) for card in cards]
    if any(check):
        return check.index(True)
    return -1

def checkForLoss(cards):
    check = [checkCard(card) for card in cards]
    if not all(check):
        return check.index(False)
    return -1

def getCardFinalScore(card, lastNum):
    unmarkedSum = sum([int(card[i][j]) for j in range(NUM_COLS) for i in range(NUM_ROWS) if card[i][j] != 'x'])
    return unmarkedSum * lastNum

### PART 1 ###
check = -1
numIndex = 0
while check == -1:
    cards = markNumAllCards(cards, nums[numIndex])
    check = checkForWin(cards)
    numIndex += 1
# print(cards[check], nums[numIndex-1])
print(getCardFinalScore(cards[check], nums[numIndex-1]))

### PART 2 ###
check = 0
numIndex = 0
while check != -1:
    cards = markNumAllCards(cards, nums[numIndex])
    prevCheck = check
    check = checkForLoss(cards)
    numIndex += 1
print(getCardFinalScore(cards[prevCheck], nums[numIndex-1]))