cards = input()

highCards = {"A": 4, "K": 3, "Q": 2, "J": 1}

DClubs = False
DDiamonds = False
DHearts = False


clubs = []
diamonds = []
hearts = []
spades = []


counterC = 0
counterD = 0
counterH = 0
counterS = 0


print("Cards Dealt              Points")


for i in range(1, len(cards)):
    if DClubs == False:
        if cards[i] != "D":
            clubs.append(cards[i])
            if cards[i] in highCards:
                counterC += highCards[cards[i]]
        else:
            DClubs = True
            if len(clubs) == 0:
                counterC += 3
            elif len(clubs) == 1:
                counterC += 2
            elif len(clubs) == 2:
                counterC += 1
            print("Clubs", *clubs, counterC)

    elif DDiamonds == False and DClubs == True:
        if cards[i] != "H":
            diamonds.append(cards[i])
            if cards[i] in highCards:
                counterD += highCards[cards[i]]
        else:
            DDiamonds = True
            if len(diamonds) == 0:
                counterD += 3
            elif len(diamonds) == 1:
                counterD += 2
            elif len(diamonds) == 2:
                counterD += 1
            print("Diamonds", *diamonds, counterD)

    elif DHearts == False and DDiamonds == True and DClubs == True:
        if cards[i] != "S":
            hearts.append(cards[i])
            if cards[i] in highCards:
                counterH += highCards[cards[i]]
        else:
            DHearts = True
            if len(hearts) == 0:
                counterH += 3
            elif len(hearts) == 1:
                counterH += 2
            elif len(hearts) == 2:
                counterH += 1
            print("Hearts", *hearts, counterH)

    else:
        spades.append(cards[i])
        if cards[i] in highCards:
            counterS += highCards[cards[i]]

if len(spades) == 0:
    counterS += 3
elif len(spades) == 1:
    counterS += 2
elif len(spades) == 2:
    counterS += 1
print("Spades", *spades, counterS)
print("                       Total ", str(counterC + counterD + counterH + counterS))