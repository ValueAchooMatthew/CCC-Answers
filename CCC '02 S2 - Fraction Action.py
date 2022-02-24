numerator = int(input())
denomenator = int(input())

based = False
if numerator%denomenator == 0:
    print(numerator//denomenator)

else:
    if numerator> denomenator:
        based = True
        whole = numerator//denomenator

    fraction = (numerator % denomenator)

    for i in range(fraction, 0, -1):
        if fraction% i == 0 and denomenator %i == 0:
            fraction = fraction//i
            denomenator = denomenator//i
    if based == True:
        print(whole, str(fraction) +"/"+str(denomenator))
    else:
        print(str(fraction) +"/"+str(denomenator))






