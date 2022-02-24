T = input()
S = input()

cycler = []

for character in S:
    cycler.append(character)



shifts = []

shifts.append(S)

for letter in cycler:
    S += letter
    S = list(S)
    
    S = S.remove(letter)
    S = str(S)
    shifts.append(S)

print(shifts)

