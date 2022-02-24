wordOne = input()
wordTwo = input()

setWordOne = list(set(wordOne))
setWordOne.sort()
setWordTwo = list(set(wordTwo))
setWordTwo.sort()

lettersOne = []
lettersTwo = []

for letter in setWordOne:
    lettersOne.append(wordOne.count(letter))
    
for letter in setWordOne:
    lettersTwo.append(wordTwo.count(letter))


if setWordTwo.count("*") > 0:

    setWordTwo.remove("*")

    check = all(item in setWordOne for item in setWordTwo)

    if check == True:
        cringe = False
        for i in range(len(lettersOne)):
            if lettersOne[i] >= lettersTwo[i]:
                pass
            else:
                print("N")
                cringe = True
                break
        
        if cringe == False:
            print("A")
        
    else:
        print("N")


else:

    check = all(item in setWordOne for item in setWordTwo)
    if check == True:
        cringe = False
        for i in range(len(lettersOne)):
            if lettersOne[i] >= lettersTwo[i]:
                pass
            else:
                print("N")
                cringe = True
                break
                
        if cringe == False:
            print("A")
    else:
        print("N")

