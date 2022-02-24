from math import ceil


x = int(input())
y = int(input())

if x == y:
    print(x)

else:
    nums = y-x + 1
    boxes = ceil(nums**(1/2))
    final = [[x]]
    stop = 0
    squares = [x]
    for i in range(x, y+1):
        
        stop +=1
        for j in range(1, stop**2 - (stop-1)**2 +1):
            squares.append(final[-1][-1] +j)
        
        final.append(squares)
        squares = []





