troutP = int(input())
pikeP = int(input())
pickerelP = int(input())
maximumP = int(input())


trouts = []
pikes = []
pics = []


for i in range(0, maximumP+1, troutP):
    trouts.append(i)

for j in range(0, maximumP+1, pikeP):
    pikes.append(j)

for k in range(0, maximumP+1, pickerelP):
    pics.append(k)


#print(trouts, pikes, pics)

combos = 0

for i in range(0, len(trouts)):
    for j in range(0, len(pikes)):
        for k in range(0, len(pics)):
            if trouts[i] + pikes[j] + pics[k] <= maximumP and trouts[i] + pikes[j] + pics[k] != 0:
                print(trouts[i]//troutP, "Brown Trout,", pikes[j]//pikeP, "Northern Pike,", pics[k]//pickerelP, "Yellow Pickerel")
                combos +=1


print("Number of ways to catch fish:", str(combos))