points = int(input())

coords = []

for i in range(points):
    coords.append(input())

areas = []

for j in range(0, len(coords)):
    for k in range(0, len(coords)):

        point1 = coords[j].split()
        point2 = coords[k].split()

        side1 = abs((int(point1[0]) - int(point2[0])))
        side2 = abs((int(point1[1]) - int(point2[1])))
        
        squarelen = max(side1, side2)
        squarearea = squarelen **2

        if squarearea != 0:
            areas.append(squarearea)

print(min(areas))