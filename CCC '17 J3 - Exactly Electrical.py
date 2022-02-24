start = input().split()
destination = input().split()
charge = int(input())

diff = abs(int(destination[0]) - int(start[0])) + abs((int(destination[1]) - int(start[1])))

if diff % 2 == 0 and charge %2 == 0 and charge >= diff:
    print("Y")

elif diff % 2 == 1 and charge %2 == 1 and charge >= diff:
    print("Y")

else:
    print("N")

