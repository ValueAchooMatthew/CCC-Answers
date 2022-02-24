boxes = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
sum = 0
n = int(input())

for i in range(n):
    chosen = int(input())
    boxes[chosen-1] = 0

for box in boxes:
    if box == 0:
        pass
    else:
        sum += box
average = sum/(10-n)

banker = int(input())

if banker > average:
    print("deal")

else:
    print("no deal")