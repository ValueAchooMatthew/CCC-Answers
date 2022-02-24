###folding


m = int(input())
n = int(input())

flippable = ["0", "1", "8"]

counter = 0

for i in range(m, n+1):
    i = str(i)
    balls = ""
    for digit in range(0, len(i)): 
        if (i[digit] in flippable and i[digit] == i[-digit-1]) or i[digit] == "6" and i[-digit-1] == "9" or i[digit] == "9" and i[-digit-1] == "6":
            balls += i[digit]

        if balls == i:
            counter +=1

print(counter)
