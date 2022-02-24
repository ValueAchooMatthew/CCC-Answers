N = int(input())

for i in range(N):
    words = [input(), input(), input()]
    
    newOrder = sorted(words, key = len)

    largest = newOrder[2]
    medium = newOrder[1]
    smallest = newOrder[0]

    if largest[0:len(medium)] != medium and largest[0:len(smallest)] != smallest and medium[0:len(smallest)] != smallest:
        if largest[-len(medium):] != medium and largest[-len(smallest):] != smallest and medium[-len(smallest):] != smallest:
            print("Yes")
        else:
            print("No")

    else:
        print("No")