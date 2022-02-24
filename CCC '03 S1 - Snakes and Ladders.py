position = 1

while True:

    movement = int(input())
    if movement == 0:
        print("You Quit!")
        break
    
    if position + movement <= 100:
        position += movement
    
    if position == 9:
        position = 34
    elif position == 40:
        position = 64
    elif position == 67:
        position = 86
    elif position == 54:
        position = 19
    elif position == 90:
        position = 48
    elif position == 99:
        position = 77

    if position == 100:
        print("You are now on square 100")
        print("You Win!")
        break
    else:    
        print("You are now on square {}" .format(position))



