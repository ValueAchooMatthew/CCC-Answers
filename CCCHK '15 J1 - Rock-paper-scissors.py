games = int(input())

AHands = input()
BHands = input()

A = AHands.split()

B = BHands.split()

aCounter = 0
bCounter = 0

for i in range(0, games):
    if A[i] == "scissors":
        if B[i] == "paper":
            aCounter += 1
        elif B[i] == "scissors":
            pass
        else:
            bCounter += 1
    elif A[i] == "rock":
        if B[i] == "paper":
            bCounter += 1
        elif B[i] == "scissors":
            aCounter += 1
        else:
            pass
    else:
        if B[i] == "rock":
            aCounter += 1
        elif  B[i] == "paper":
            pass
        else:
            bCounter += 1

print(aCounter, bCounter)








