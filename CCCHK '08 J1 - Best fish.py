fishesC = int(input())

CPoints = []
NPoints = []

for i in range(fishesC):
    fish = input()
    space = fish.index(" ")
    weight = int(fish[:space])
    height = int(fish[space:])
    CPoints.append(weight*height)
    
fishesN = int(input())

for i in range(fishesN):
    fish = input()
    space = fish.index(" ")
    weight = int(fish[:space])
    height = int(fish[space:])
    NPoints.append(weight*height)

bestC = max(CPoints)
bestN = max(NPoints)

if bestC > bestN:
    print("Casper")
elif(bestC < bestN):
    print("Natalie")
else:
    print("Tie")
