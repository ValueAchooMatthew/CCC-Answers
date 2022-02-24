button = "lol"

songs = ["A", "B", "C", "D", "E"]

while button != "4":
    button = input()
    times = int(input())

    if button == "1":
        for i in range(times):
            songs[0], songs[1], songs[2], songs[3], songs[4] = songs[1], songs[2], songs[3], songs[4], songs[0]
    elif button == "2":
        for i in range(times):
            songs[0], songs[1], songs[2], songs[3], songs[4] = songs[4], songs[0], songs[1], songs[2], songs[3]
    elif button == "3":
        for i in range(times):
            songs[0], songs[1] = songs[1], songs[0]

print(*songs)
        



