counterA = 0
counterB = 0

cards = []
highcards = ["jack", "queen", "king", "ace"]


for i in range(52):
    cards.append(input())



for j in range(52):
    if j <= 47 and cards[j] == "ace" and cards[j+1] not in highcards and cards[j+2] not in highcards and cards[j+3] not in highcards and cards[j+4] not in highcards:
        if j % 2 == 1:
            counterB += 4
            print("Player B scores 4 point(s).")
        else:
            counterA += 4
            print("Player A scores 4 point(s).")
    elif j <= 48 and cards[j] == "king" and cards[j+1] not in highcards and cards[j+2] not in highcards and cards[j+3] not in highcards:
        if j % 2 == 1:
            counterB += 3
            print("Player B scores 3 point(s).")
        else:
            counterA += 3
            print("Player A scores 3 point(s).")
    elif j <= 49 and cards[j] == "queen" and cards[j+1] not in highcards and cards[j+2] not in highcards:
        if j % 2 == 1:
            counterB += 2
            print("Player B scores 2 point(s).")
        else:
            counterA += 2
            print("Player A scores 2 point(s).")
    elif j <= 50 and cards[j] == "jack" and cards[j+1] not in highcards:
        if j % 2 == 1:
            counterB += 1
            print("Player B scores 1 point(s).")
        else:
            counterA += 1
            print("Player A scores 1 point(s).")


print("Player A:", counterA, "point(s).")
print("Player B:", counterB, "point(s).")