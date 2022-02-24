bowl1, bowl2, bowl3 = int(input()), int(input()), int(input())

if((bowl1 > bowl2) and (bowl2 > bowl3)) or ((bowl3 > bowl2) and (bowl2 > bowl1)):
    print(bowl2)

elif((bowl2 > bowl1) and (bowl1 > bowl3)) or ((bowl3 > bowl1) and bowl1 > bowl2):
    print(bowl1)

else:
    print(bowl3)