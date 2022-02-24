phrase = input()

menu = ["ABCDEF", "GHIJKL", "MNOPQR", "STUVWX", "YZ -."]

counterx = 0
countery = 0
pastx = 0
pasty = 0

for character in phrase:
    for ycoord in range(len(menu)):
        try:
            xcoord = menu[ycoord].index(character)
            counterx += abs(xcoord - pastx)
            countery += abs(ycoord- pasty)
            pastx = xcoord
            pasty = ycoord
            break

        except:
            pass
    

enterdiffx, enterdiffy = abs(5 - xcoord), abs(4 - ycoord)

print(int(counterx) + int(countery) +int(enterdiffx) +int(enterdiffy))