N = int(input())

topRow = input().split()
bottomRow = input().split()

groupings = {}


cringe = False
for i in range(N):
    if topRow[i] == bottomRow[i]:
        cringe = True
        print("bad")
        break

    elif (topRow[i] in groupings and groupings[topRow[i]] != bottomRow[i]) or (bottomRow[i] in groupings and groupings[bottomRow[i]] != topRow[i]):
        cringe = True
        print("bad")
        break

    else:
        groupings[topRow[i]] = bottomRow[i]
        groupings[bottomRow[i]] = topRow[i]


if cringe == False:
    print("good")











