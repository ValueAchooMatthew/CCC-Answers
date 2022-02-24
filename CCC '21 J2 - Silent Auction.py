numberOfBids = int(input())

bids = []
names = []


for i in range(2*numberOfBids):
    if i % 2 == 0:
        names.append(input())
    else:
        bids.append(int(input()))

winner = max(bids)

print(names[bids.index(winner)])