N = int(input())

pointsx = []
pointsy = []
for i in range(N):

    point = input()
    #print(point)
    comma = point.index(",")
    pointsx.append(int(point[:comma]))
    pointsy.append(int(point[comma+1:]))

bottomLeftX, bottomLeftY = min(pointsx) -1, min(pointsy)-1
print(str(bottomLeftX) +"," +str(bottomLeftY))

topRightX, topRightY = max(pointsx)+1, max(pointsy)+1
print(str(topRightX) +"," +str(topRightY))
