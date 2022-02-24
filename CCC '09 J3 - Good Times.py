ot = int(input())

minutes = ot%100
hours = ot//100

print(ot, "in Ottawa")

if hours - 3 < 0:
    print((hours + 21)*100 + minutes, "in Victoria")

else:
    print((hours - 3)*100 + minutes, "in Victoria")

if hours - 2 < 0:
    print((hours + 22)*100 + minutes, "in Edmonton")

else:
    print((hours - 2)*100 + minutes, "in Edmonton")

if hours - 1 < 0:
    print((hours + 23)*100 + minutes, "in Winnipeg")

else:
    print((hours - 1)*100 + minutes, "in Winnipeg")

print(ot, "in Toronto")

if hours == 23:
    print(minutes, "in Halifax")

else:
    print((hours + 1)*100 + minutes, "in Halifax")

hours += 1
minutes += 30
if minutes >= 60:
    hours += 1
    minutes -= 60
    if hours >= 24:
        print((hours-24)*100 +minutes, "in St. John's")
    else:
        print((hours*100 + minutes), "in St. John's")

else:
    if hours >= 24:
        print((hours-24)*100 +minutes, "in St. John's")
    else:
        print((hours*100 + minutes), "in St. John's")