antanae = int(input())
eyes = int(input())

aliens = ["TroyMartian", "VladSaturnian", "GraemeMercurian"]

description = []

if antanae >= 3 and eyes <= 4:
    description.append(aliens[0])

if antanae <= 6 and eyes >= 2:
    description.append(aliens[1])

if antanae <= 2 and eyes <= 3:
    description.append(aliens[2])

print(*description, sep ="\n")
    
