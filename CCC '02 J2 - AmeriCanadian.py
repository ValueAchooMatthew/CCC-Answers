translation = "lol"

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]

while translation != "quit!":
    translation = input()
    if len(translation) > 4 and translation[-3] in consonants and translation[-2:] == "or":
        translation = translation[0:-2]
        print(translation +"our")
    elif translation != "quit!":
        print(translation)


