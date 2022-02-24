N = int(input())

countA = 100
countD = 100

for i in range(N):
    roll = input()
    if int(roll[0]) > int(roll[2]):
        countD -= int(roll[0])
    elif int(roll[0]) < int(roll[2]):
        countA -= int(roll[2])
    else:
        pass

print(countA)
print(countD)




