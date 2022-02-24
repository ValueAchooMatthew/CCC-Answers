adjectives = int(input())
nouns = int(input())

nounsList = []
adjectivesList = []

for i in range(adjectives):
    y = input()
    adjectivesList.append(y)


for i in range(nouns):
    x = input()
    nounsList.append(x)


for i in range(len(adjectivesList)):
    for j in range(len(nounsList)):
        print(adjectivesList[i], "as", nounsList[j])



