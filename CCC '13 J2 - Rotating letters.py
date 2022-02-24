word = input()

length = len(word)

false = 0

for i in range(length):
    letter = word[i]
    if letter != "I" and letter != "O" and letter != "S" and letter != "H" and letter != "Z" and letter != "X" and letter != "N":
        false += 1
    else:
        pass

if false > 0:
    print("NO")

else:
    print("YES")