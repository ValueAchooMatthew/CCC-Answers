score = []

score.append(input()), score.append(input()), score.append(input()), score.append(input()), score.append(input()), score.append(input())

count = score.count("W")

if count >= 5:
    print("1")
elif count == 3 or count == 4:
    print("2")
elif count == 1 or count == 2:
    print("3")
else:
    print("-1")
