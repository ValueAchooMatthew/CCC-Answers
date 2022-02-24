instruction = ""
directions = []
counter = -1

while instruction != "99999":
    instruction = input()
    counter +=1
    
    
    if instruction != "99999":
        if (int(instruction[0]) + int(instruction[1])) % 2 == 0 and (int(instruction[0]) + int(instruction[1])) != 0:
            directions.append("right")

        elif (int(instruction[0]) + int(instruction[1])) % 2 == 1 and (int(instruction[0]) + int(instruction[1])) != 0:
            directions.append("left")

        else:
            directions.append(directions[-1])

        print(directions[counter], instruction[2:])

