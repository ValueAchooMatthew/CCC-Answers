row1 = input().split()
row2 = input().split()
row3 = input().split()
row4 = input().split()

masterRow =(row1, row2, row3, row4)

rowSums = []

columnSums = []

for i in masterRow:
    rowSum = 0
    for j in i:
        rowSum += int(j)

    rowSums.append(str(rowSum))

for k in range(0, 4):
    columnSum = 0
    for l in masterRow:
        columnSum += int(l[k])

    columnSums.append(str(columnSum))

if rowSums.count(rowSums[0]) == 4 and columnSums.count(columnSums[0]) == 4 and rowSums[0] == columnSums[0]:
    print("magic")

else:
    print("not magic")
