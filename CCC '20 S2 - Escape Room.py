from math import ceil


M = int(input())
N = int(input())

maze = []


for i in range(M):
    maze.append(list(map(int, input().split())))


pos = [M, N]
visited = []
root = []


while True:

    if pos == [0, 0]:
        print("yes")
        break

    else:
        factors = []
        number = maze[pos[0]-1][pos[1]-1]
        if number <= M:
            factors.append(number, 1)
        
        if number <= N:
            factors.append(1, number)

        for i in range(2, ceil(number**(1/2))+2):
            if number % i == 0:
                if i <= M and int(number/i) <= N:
                    factor = [i, int(number/i)]
                    factors.append(factor)
                
                if int(number/i) <= M and i <= N and i != int(number/i):
                    factor = [int(number/i), i]

        if len(factors) == 0:
            if len(visited) == 0:
                print("no")

            else:
                visited.append(pos)
                pos = root[-1]

        else:

            for factor in factors:
                if factor not in visited:
                    pos = factor
                    visited.append(factor)
                    root.append(factor)
                    break
                
