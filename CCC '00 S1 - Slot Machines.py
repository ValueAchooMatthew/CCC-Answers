coins = int(input())

machineOne = int(input())
machineTwo = int(input())
machineThree = int(input())

counter = 0

while True:
    if coins > 0:
        coins -= 1
        machineOne += 1
        counter += 1
        if machineOne % 35 == 0:
            coins += 30
    else:
        break

    if coins > 0:
        coins -= 1
        machineTwo += 1
        counter += 1
        if machineTwo % 100 == 0:
            coins += 60
    else:
        break
    
    if coins > 0:
        coins -= 1
        machineThree += 1
        counter += 1
        if machineThree % 10 == 0:
            coins += 9
    else:
        break

print("Martha plays", counter, "times before going broke.")
