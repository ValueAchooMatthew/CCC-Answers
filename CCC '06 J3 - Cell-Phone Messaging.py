time = {'a': 1, 'b': 2, 'c': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1, 'h': 2, 'i': 3, 'j': 1, 'k': 2, 'l': 3, 'm': 1, 'n': 2, 'o': 3, 'p': 1, 'q': 2, 'r': 3, 's': 4, 't': 1, 'u': 2, 'v': 3, 'w': 1, 'x': 2, 'y': 3, 'z': 4}
buttons = {'a': 1, 'b': 1, 'c': 1, 'd': 2, 'e': 2, 'f': 2, 'g': 3, 'h': 3, 'i': 3, 'j': 4, 'k': 4, 'l': 4, 'm': 5, 'n': 5, 'o': 5, 'p': 6, 'q': 6, 'r': 6, 's': 6, 't': 7, 'u': 7, 'v': 7, 'w': 8, 'x': 8, 'y': 8, 'z': 8}

word = ""

while word != "halt":
    counter = 0
    listed = []
    word = input()
    if word != "halt":
        for character in word:
            listed.append(character)
        
        for i in range(len(listed)):
            if (i != len(listed)-1) and buttons[listed[i]] == buttons[listed[i+1]]:
                counter += time[listed[i]]
                counter += 2 
            else:
                counter += time[listed[i]]
        
        print(counter)
    
    
    
    