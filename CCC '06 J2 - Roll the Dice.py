m = int(input())
n = int(input())

counter = 0

for i in range(1, m+1):
    for j in range(1, n+1):
        if i + j == 10:
            counter += 1
        else:
            pass

if counter == 1:
    print("There is 1 way to get the sum 10." )
    

else: 
    print("There are", counter, "ways to get the sum 10.")
    

