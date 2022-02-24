user = input()

startDay = int(user[0])
days = int(user[-2:])

count = 0

week = []

startSpace = "    "
start = True

print("Sun Mon Tue Wed Thr Fri Sat" )

while count < days:

    if (count + startDay) % 8 != 0:
        count += 1
        if count < 10 and start == True:
            week.append(startSpace*(startDay-1))
            week.append("")
            week.append(count)
            start = False
        elif count < 10 and start == False:
            week.append(" ")
            week.append(count)
        else:
            week.append("")
            week.append(count)

    else:
        print(*week)
        week = []
        count += 1
        startDay += 1
        if count < 10:
            week.append(" ")
            week.append(count)
        else:
            week.append("")
            week.append(count)

print(*week)

