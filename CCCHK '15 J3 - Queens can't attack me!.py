start = list(map(int, input().split()))

size, queens = start[0], start[1]

occupiedx = []
occupiedy = []

for i in range(queens):
    intermed = list(map(int, input().split()))
    occupiedx.append(intermed[0])
    occupiedy.append(intermed[1])

counter = 0

for j in range(1, size + 1):
    for k in range(1, size + 1):
        if j in occupiedx:
            counter += 1
        elif k in occupiedy:
            counter += 1

        else:
            for l in range(len(occupiedx)):
                if abs((k - occupiedy[l]) / (j - occupiedx[l])) == 1:
                    counter += 1
                    break

print(size**2 - counter)
