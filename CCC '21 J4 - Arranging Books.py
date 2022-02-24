import sys

books = list(sys.stdin.readline())[:-1]

length = len(books)

counter = 0
repeats = -1

final = []
if length != 1:
    while True:
        repeats += 1
        for i in range(length):
            if books[i] == "S":
                for j in range(-1, i - length, -1):
                    if books[j] == "L":
                        books[i], books[j] = "L", "S"
                        counter += 1
                        break
                    elif books[j] == "M":
                        books[i], books[j] = "M", "S"
                        counter += 1
                        break

        for i in range(-1, -length, -1):
            if books[i] == "L":
                for j in range(-length, i, +1):
                    if books[j] == "S":
                        books[j], books[i] = "L", "S"
                        counter += 1
                        break
                    elif books[j] == "M":
                        books[j], books[i] = "L", "M"
                        counter += 1
                        break
                    
            
        final.append(str(books))

        if repeats >= 2 and final[-1] == final[-2]:
            print(counter)
            break
        
else:
    print(0)