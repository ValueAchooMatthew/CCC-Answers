import sys
N = int(input())

swifts = list(map(int, sys.stdin.readline().split()))
semaphores = list(map(int, sys.stdin.readline().split()))

swiftPoints = 0
semaphorePoints = 0

days = []
cringe = True

for i in range(0, N):
    swiftPoints += swifts[i]
    semaphorePoints += semaphores[i]

    if swiftPoints == semaphorePoints:
        days.append(i + 1)
        cringe = False
    
if cringe == False:
    print(max(days))
else:
    print(0)