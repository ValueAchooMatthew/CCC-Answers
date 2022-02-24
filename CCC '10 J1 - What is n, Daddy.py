n = int(input())

hand1 = n
hand2 = 0

counter = 0
while True:
    if hand1 <= 5 and hand2 <=5:
        counter += 1
    hand1 -= 1
    hand2 += 1
    if hand1 < hand2:
        break

print(counter)