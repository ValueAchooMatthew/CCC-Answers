word = input()

counters = []
counter = 1

letter = 0
lastletter = 0
nextletter = 0

for letter in range(len(word)):

    if letter != 0:
        lastletter = letter -1

    if nextletter != len(word) -1:
        nextletter = letter + 1

    while word[lastletter] == word[nextletter] and lastletter != nextletter and lastletter > 0:
        counter += 2
        if lastletter > 0:
            lastletter -= 1
        else:
            counter += 1
            break
        if nextletter <len(word)-1:
            nextletter += 1
        else:
            counter += 1
            break

    while word[letter] == word[nextletter] and letter != nextletter:
        counter += 1
        if letter >0:
            letter -= 1
        else:
            counter +=1
            break

        if nextletter <len(word)-1:
            nextletter += 1
        else:
            counter += 1
            break
    
    while word[letter] == word[lastletter] and letter != lastletter and lastletter > 0:
        counter +=1
        if lastletter > 0:
            lastletter -= 1
        else:
            counter += 1
            break
        
        if letter < len(word)-1:
            letter += 1
        else:
            counter += 1
            break

    else:
        counters.append(counter)
        counter = 1
    

print(max(counters))
