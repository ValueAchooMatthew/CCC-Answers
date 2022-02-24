villages = []
neighbourhoods = []

N = int(input())
for i in range(N):
    villages.append(int(input()))

villages.sort()

for j in range(1, N-1):
    village = villages[j]
    distanceLeft = (village - villages[j-1])/2
    distanceRight = (villages[j+1] - village)/2
    neighbourhoods.append(distanceLeft + distanceRight)


print(float(min(neighbourhoods)))
