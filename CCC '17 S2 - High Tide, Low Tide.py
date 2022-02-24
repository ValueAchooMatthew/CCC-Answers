from math import ceil, floor


N = int(input())

records = list(map(int, input().split()))

records.sort()

high = records[ceil(N/2):]
low = records[:ceil(N/2)]

final = []

for i in range(N):
    if i % 2 == 0:
        final.append(low[-1])
        low.remove(low[-1])
    else:
        final.append(high[0])
        high.remove(high[0])
    

print(*final)
