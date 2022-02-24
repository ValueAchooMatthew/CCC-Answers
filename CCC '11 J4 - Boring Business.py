position = [-1, -5]
intersect = False
dug = [[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], [3, -3], [3, -4], [3, -5], [4, -5],
       [5, -5], [5, -4], [5, -3], [6, -3], [7, -3], [7, -4], [7, -5], [7, -6], [7, -7],
       [6, -7], [5, -7], [4, -7], [3, -7], [2, -7], [1, -7], [0, -7], [-1, -7], [-1, -6]
               ] 
while not intersect:
    instruction = input().split()
    if instruction[0] == "q":
        break
    
    else:
        original = position
        direction = instruction[0]
        magnitude = int(instruction[1])
        if direction == "l":
            for i in range(1, magnitude+1):
                dug.append(position)
                new = []
                new.append(position[0] - 1)
                new.append(position[1])
                if new in dug:
                    print(original[0] - magnitude, original[1], "DANGER")
                    intersect = True
                    break

                position = new


        elif direction == "r":
            for i in range(1, magnitude+1):
                dug.append(position)
                new = []
                new.append(position[0] + 1)
                new.append(position[1])
                if new in dug:
                    print(str(original[0] + magnitude), str(position[1]), "DANGER")
                    intersect = True
                    break

                position = new


        elif direction == "d":
            for i in range(1, magnitude+1):
                dug.append(position)
                new = []
                new.append(position[0])
                new.append(position[1] -1)
                if new in dug:
                    print(original[0], original[1] - magnitude, "DANGER")
                    intersect = True
                    break

                position = new

    
        else: 
            for i in range(1, magnitude+1):
                dug.append(position)
                new = []
                new.append(position[0])
                new.append(position[1] + 1)
                if new in dug:
                    print(original[0], original[1] + magnitude, "DANGER")
                    intersect = True
                    break
        
                position = new

        if not intersect:
            print(*position, "safe")

