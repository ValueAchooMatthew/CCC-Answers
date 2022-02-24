N = int(input())

for i in range(N):
    line = list(input())
    final = []  
    counter = 1

    for element in range(len(line)):

        if element != (len(line)-1) and line[element] == line[element + 1]:
            counter +=1
        
        else:
            final.append(counter)
            final.append(line[element])
            counter = 1

    print(*final)

    
