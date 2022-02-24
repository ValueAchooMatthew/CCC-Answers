#Occurs every 60 years
#Smarter work around

yearX = int(input())
yearY = int(input())

for year in range(yearX, yearY +1):
    diff = year-yearX
    if diff % 4 == 0 and diff % 5 == 0 and diff % 3 == 0:
        print("All positions change in year", year)