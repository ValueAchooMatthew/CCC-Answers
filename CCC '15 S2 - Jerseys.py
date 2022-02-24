J = int(input())
A = int(input())

##positions

jerseys = []
athletes = []
nums = []


for i in range(J):
    jerseys.append(input())

for i in range(A):
    athlete, num = input().split()
    athletes.append(athlete)
    nums.append(int(num))


#U for used
#Error: removing, maybe try replacing?
###Try greedy algorithm

counter = 0

LDone = False
MDone = False

while True:
    if LDone == False:
        try:
            position = athletes.index("L")
            size, number = "L", nums[position]
            if jerseys[number-1] == size:
                counter += 1
                athletes[position] = "U"
                nums[position] = 0
                jerseys[jerseys.index(int(number) +1)] = "U"
            else:
                athletes[position] = "U"
                nums[position] = 0
        except:
            LDone = True
    
    elif LDone == True and MDone == False:
        try:
            position = athletes.index("M")
            size, number = "M", nums[position] 
            if jerseys[number -1] == size or jerseys[number-1]  == "L":
                counter += 1
                athletes[position] = "U"
                nums[position] = 0
                jerseys[number-1] = "U"
            else:
                athletes[position] = "U"
                nums[position] = 0
        except:
            MDone = True

    else:
        try:
            position = athletes.index("S")
            size, number = "S", nums[position] 
            if jerseys[number -1] == size or jerseys[number-1]  == "L" or jerseys[number] == "M":
                counter += 1
                athletes[position] = "U"
                nums[position] = 0
                jerseys[number-1] = "U"
            else:
                athletes[position] = "U"
                nums[position] = 0
        except:
            break


print(counter)


