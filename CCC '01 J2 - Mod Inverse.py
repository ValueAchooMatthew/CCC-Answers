x = int(input())
m = int(input())

prints = []

for i in range(0, m+1):
    if (x * i) % m == 1:
        prints.append(i)

if len(prints) > 0:
    print(*prints)

else:
    print("No such integer exists.")