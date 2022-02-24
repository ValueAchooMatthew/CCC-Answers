pinpad = {"A": 2, "B": 2, "C": 2, "D": 3, "E": 3, "F": 3, "G": 4, "H": 4, "I": 4, "J": 5, "K": 5, "L": 5, "M": 6,
          "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7, "S": 7, "T": 8, "U": 8, "V": 8, "W": 9, "X": 9, "Y": 9, "Z": 9}

for i in range(int(input())):
    phoneNumber = list(input())
    conversion = []
    for k in range(phoneNumber.count("-")):
        phoneNumber.remove("-")

    for character in range(10):
        if phoneNumber[character].isdigit() == True:
            conversion += str(phoneNumber[character])
        else:
            if phoneNumber[character] == "-":
                character += 1

            conversion += str(pinpad[phoneNumber[character]])
    conversion.insert(3, "-")
    conversion.insert(7, "-")
    print(*conversion, sep = "")