from math import floor


while True:
    radius = int(input())
    pennies = 0
    if radius == 0:
        break
    else:
        for i in range(radius, -radius-1, -1):
            if i == 0:
                pennies += 2*radius +1
            elif i == radius or i == -radius:
                pennies += 1

            else:
                side = floor((( radius**2 - i**2))**(1/2))
                pennies += 2 *side +1

    print(pennies)


