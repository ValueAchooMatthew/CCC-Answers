c, r = list(map(int, input().split()))
positionx = 0
positiony = 0
while True:
    
    movement = input()

    if movement == "0 0":
        break
    else:
        a, b = list(map(int, movement.split()))
        if positionx + a >= 0 and positionx + a <= c:
            positionx += a
        elif positionx + a < 0:
            positionx = 0
        else:
            positionx = c

        if positiony + b >= 0 and positiony + b <= r:
            positiony += b
        elif positiony + b < 0:
            positiony = 0
        else:
            positiony = r
        
        print(positionx, positiony)



