year = input()

original = year


while True:

    cringe = False
    listed = []

    components = list(map(int, list(str(year))))

    year = int(year)

    for number in components:
        if number in listed:
            cringe = True
            break
        else:
            listed.append(number)

    if cringe == False and year != int(original):
        print(year)
        break
    
    else:
        year +=1

