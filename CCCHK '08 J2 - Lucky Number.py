n = int(input())


for i in range(n):
    birthday = input()
    while len(birthday) != 1:
        birthdaynew = 0
        birthdaydigits = []
        for i in range(0, len(birthday)):
            birthdaydigits.append(int(birthday[i]))

        for i in range(0, len(birthdaydigits)):
            birthdaynew += birthdaydigits[i] 

        birthday = str(birthdaynew)
        
    print(birthday)