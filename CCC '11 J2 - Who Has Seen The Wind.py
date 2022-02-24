humidity = int(input())
maximum = int(input())

time = 0

for t in range(1, maximum):
    A = -6*(t)**4 + humidity*(t)**3 + 2*(t)**2 + t
    if A <= 0:
        time = t
        break

if time == 0:
    print("The balloon does not touch ground in the given time.")

else:
    print("The balloon first touches ground at hour:")
    print(time)