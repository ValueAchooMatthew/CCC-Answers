N = int(input())

poems = []

for i in range(N):
    stanzas = []
    for j in range(4):
        stanzas.append(input())

    poems.append(stanzas)

vowels = ["a", "e", "i", "o", "u"]


for poem in poems:
    based = False
    syllables = []
    for line in poem:
        lastWord = (str(line).split()[-1]).lower()
        for i in range(-1, -len(lastWord)-1, -1):
            if lastWord[i] in vowels:
                syllables.append(lastWord[i:])
                based = True
                break
        if based == False:
            syllables.append(lastWord)

    if syllables[0] == syllables[1] and syllables[0] == syllables[2] and syllables[0] == syllables[3]:
        print("perfect")
    
    elif syllables[0] == syllables[1] and syllables[2] == syllables[3]:
        print("even")
    
    elif syllables[0] == syllables[2] and syllables[1] == syllables[3]:
        print("cross")
    
    elif syllables[0] == syllables[3] and syllables[1] == syllables[2]:
        print("shell")
    
    else:
        #print(poems[1][2], poems[1][3])
        print("free")







