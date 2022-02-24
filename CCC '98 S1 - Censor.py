for i in range(int(input())):
    line = list(input().split())
    for i in range(len(line)):
        if len(line[i]) == 4:
            line.remove(line[i])
            line.insert(i, "****")

    print(*line)