K = int(input())
word = input()

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"
, "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

output = []

for i in range (len(word)):
    S = 3*(i+1) + K

    output += alphabet[alphabet.index(word[i]) - S]
    
end = "".join(output)
print(end)
