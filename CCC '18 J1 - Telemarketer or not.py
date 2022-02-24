id = []

id.append(int(input())), id.append(int(input())), id.append(int(input())), id.append(int(input()))

if (id[0] == 8 or id[0] == 9) and (id[3] == 8 or id[3] == 9) and (id[1] == id[2]):
    print("ignore")

else:
    print("answer")
