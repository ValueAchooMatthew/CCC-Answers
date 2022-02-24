start = int(input())
k = int(input())

shiftySum = 0

for i in range(0, k+1):
    shiftySum += start * 10**i

print(shiftySum)