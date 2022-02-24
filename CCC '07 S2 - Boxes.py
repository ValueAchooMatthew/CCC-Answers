m = int(input())

### Volume to dimensions so it is easier to take values and sort with collections

boxesVol = []
boxesDim = []
for i in range(m):
    box = list(map(int, input().split()))
    boxesDim.append(box)
    boxesVol.append(box[0] * box[1] * box[2])

originalDim = []
 
while True:
    for i in range(m-1):

        if boxesVol[i] > boxesVol[i+1]:
            boxesDim[i], boxesDim[i+1] = boxesDim[i+1], boxesDim[i]
            boxesVol[i], boxesVol[i+1] = boxesVol[i+1], boxesVol[i]
    
    if originalDim == boxesDim:
        break
    
    else:
        originalDim = boxesDim.copy()



n = int(input())

products = []

for i in range(n):
    products.append(list(map(int, input().split())))

for product in products:

    fits = False
    productx, producty, productz = product

    for i in range(m):
        box = boxesDim[i]
        if box[0] >= productx:
            if box[1] >= producty:
                if box[2] >= productz:
                    print(boxesVol[i])
                    fits = True
                    break

            if box[1] >= productz and fits == False:
                if box[2] >= producty:
                    print(boxesVol[i])
                    fits = True
                    break

        if box[0] >= producty and fits == False:
            if box[1] >= productx:
                if box[2] >= productz:
                    print(boxesVol[i])
                    fits = True
                    break

            if box[1] >= productz and fits == False:
                if box[2] >= productx:
                    print(boxesVol[i])
                    fits = True
                    break
        
        if box[0] >= productz and fits == False:
            if box[1] >= productx:
                if box[2] >= producty:
                    print(boxesVol[i])
                    fits = True
                    break
            
            if box[1] >= producty and fits == False:
                if box[2] >= productx:
                    print(boxesVol[i])
                    fits = True
                    break

    if fits == False:
        print("Item does not fit.")
