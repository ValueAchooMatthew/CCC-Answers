N = int(input())

day1 = input()
day2 = input()

counter = 0
for i in range(0, N):
    if day1[i] == "C" and day2[i] == "C":
        counter += 1

print(counter)


###more efficient
#for i in range(0, N):
#    if "C" in day1 == day2:
#        counter += 1

#print(counter)
