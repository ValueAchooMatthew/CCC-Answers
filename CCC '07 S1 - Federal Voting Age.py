N = int(input())

for _ in range(N):
    year, month, day = list(map(int, input().split()))


    if 2007 - year > 18:
        print("Yes")
    
    elif 2007 - year < 18:
        print("No")
    
    else:
        if month > 2:
            print("No")
        elif month == 1:
            print("Yes")
        else:
            if day <= 27:
                print("Yes")
            else:
                print("No")

