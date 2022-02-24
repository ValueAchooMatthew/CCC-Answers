maximum = int(input())
infected = int(input())
transmitted = int(input())
total = 0
days = -1
#if transmitted > 1:
#    days = floor(log(maximum/infected, transmitted))
#    print(days)

while total <= maximum:
    days += 1
    total += infected*(transmitted)**days

print(days)