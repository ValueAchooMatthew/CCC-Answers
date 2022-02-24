from collections import Counter

n = int(input())

names = []
score = []

done = False

if n == 0:
    pass
    
elif n == 1:
    names, *specs = input().split()
    print(names)


else:
    for i in range(n):
        name, *specs = input().split() 
        names.append(name)
        score.append(2 * int(specs[0]) + 3 * int(specs[1]) + int(specs[2]))

    maximum = max(score)
    numMax = Counter(score)
    final = []
    if numMax[maximum] > 1:
        
        for i in range(numMax[maximum]):
            final.append(names[score.index(maximum)])
            score[score.index(maximum)] = -1
        
        final.sort()
        
    else:
        final.append(names[score.index(maximum)])
        score[score.index(maximum)] = -1
    
    if len(final) == 2:
        print(final[0])
        print(final[1])
    
    else:
        maximum = max(score)
        numMax = Counter(score)
        if numMax[maximum] > 1:
            tieBreaker = []
            for i in range(numMax[maximum]):
                tieBreaker.append(names[score.index(maximum)])
                score[score.index(maximum)] = -1
            
            tieBreaker.sort()
            final.append(tieBreaker[0])
            print(final[0])
            print(final[1])

        else:
            final.append(names[score.index(maximum)])
            score[score.index(maximum)] = -1
            print(final[0])
            print(final[1])





    


    


