word = list(input())
counters = []

for i in range(1, 2*len(word)-1, 2):
    word.insert(i, "/")

#print(word)


for j in range(1, len(word)-2):
    offset = 1
    counter = 0
    
    if word[j] != "/":
        counter += 1

    while word[j-offset] == word[j+offset]:

        if word[j-offset] == "/" or word[j+offset] == "/":
            offset += 1
        else:
            counter +=2
            if (j - offset) > 0 and (j + offset) < len(word)-2:
                offset += 1
            else:
                break
    
    counters.append(counter)

print(max(counters))
    

