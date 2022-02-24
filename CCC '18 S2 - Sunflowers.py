n = int(input())

sunflowers = []

for i in range(n):
    sunflowers.append(list(map(int, input().split())))

###First Check

cringe = False
cringe2 = False
for i in range(0, n-1):
    if sunflowers[i][0] > sunflowers[i+1][0]:
        cringe = True
        break
        


for i in range(n):
    if cringe2 == False:
        for j in range(0, n-1):
            if sunflowers[i][j] > sunflowers[i][j+1]:
                cringe2 = True
                break
    else:
        break




final = []



if cringe == False and cringe2 == False:
    for plants in sunflowers:
        print(*plants)

elif cringe == False and cringe2 == True:
    
    for j in range(1, n+1):
        intermed = []
        for i in range(n):
            intermed.append(sunflowers[i][-j])

        final.append(intermed)
    
    for plants in final:
        print(*plants)


elif cringe == True and cringe2 == False:

    
    for i in range(n):
        intermed = []
        for j in range(-1, -n-1, -1):
            intermed.append(sunflowers[j][i])

        final.append(intermed)

    for plants in final:
        print(*plants)

else:
    for i in range(-1, -n-1, -1):
        plant = sunflowers[i]
        intermed = []
        for j in range(-1, -n-1, -1):
            intermed.append(plant[j])

        final.append(intermed)
    
    for plants in final:
        print(*plants)

