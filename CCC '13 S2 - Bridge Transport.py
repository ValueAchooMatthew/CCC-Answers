maxWeight = int(input())
cars = int(input())

trains = []

for i in range(cars):
    trains.append(int(input()))

sums = []

cringe = False
if cars >= 4:
    weight = 0
    for i in range(4):
        weight += trains[i]
        if weight <= maxWeight:
            pass
        else:
            print(i) 
            cringe = True
            break

    if cringe == False:
        sums.append(weight)
        for i in range(1, cars -3, 1):
            sums.append(trains[i] + trains[i+1] + trains[i+2] + trains[i+3])

        crossed = 0
        for i in range(len(sums)):
            if sums[i] <= maxWeight:
                if crossed == 0:
                    crossed = 4
                else:
                    crossed +=1
            else:
                break
    
        print(crossed)


else:
    weight = 0
    for i in range(cars):
        weight += trains[i]
        if weight <= maxWeight:
            pass
        else:
            print(i)
            break
