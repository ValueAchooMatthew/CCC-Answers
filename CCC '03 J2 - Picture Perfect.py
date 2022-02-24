C = "lol"



while C != 0:
    perims = []
    dimensions = []

    C = int(input())
    for dimension1 in range(1, C+1):
        if C % dimension1 == 0:
            dimension2 = C // dimension1
            perims.append(dimension1*2 + dimension2*2)
            dimensions.append(dimension1)
            dimensions.append(dimension2)

    if C != 0:
        minPerim = min(perims)
        dimension1, dimension2 = dimensions[perims.index(minPerim)*2], dimensions[perims.index(minPerim)*2+1]
        print("Minimum perimeter is", minPerim, "with dimensions", dimension1, "x", dimension2)



