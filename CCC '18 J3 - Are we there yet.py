dists = list(map(int, input().split()))


c = [0]
for i in range(0, 4):
    c.append(c[i] + dists[i])


for i in range(0, 5):
    r = []
    for j in range(0, 5):
        distance = abs(c[j] - c[i])
        r.append(distance)
    print(*r)

