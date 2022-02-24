alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vowels = "aeiou"

word = input()
final = []

for character in word:
    diff = []
    if character not in vowels:
        final.append(character)
    place = alphabet.index(character)
    for vowel in vowels:
        diff.append(abs(place- alphabet.index(vowel)))
    final.append(vowels[diff.index(min(diff))])

    if character not in vowels:
        if place != 25 and alphabet[place+1] not in vowels:
            final.append(alphabet[place+1])
        elif place == 25:
            final.append("z")
        else:
            final.append(alphabet[place+2])
    

print(*final, sep= "")