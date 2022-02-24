mom = input()
dad = input()

alleles = []

combos = []



if mom.count("A") == 2 or dad.count("A") == 2:
    combos.append("A")

elif mom.count("a") == 2 and dad.count("a") == 2:
    combos.append("a")

else:
    combos.append("A")
    combos.append("a")
    
if mom.count("B") == 2 or dad.count("B") == 2:
    combos.append("B")

elif mom.count("b") == 2 and dad.count("b") == 2:
    combos.append("b")

else:
    combos.append("B")
    combos.append("b")
    
if mom.count("C") == 2 or dad.count("C") == 2:
    combos.append("C")

elif mom.count("c") == 2 and dad.count("c") == 2:
    combos.append("c")

else:
    combos.append("C")
    combos.append("c")
    
if mom.count("D") == 2 or dad.count("D") == 2:
    combos.append("D")

elif mom.count("d") == 2 and dad.count("d") == 2:
    combos.append("d")

else:
    combos.append("D")
    combos.append("d")

if mom.count("E") == 2 or dad.count("E") == 2:
    combos.append("E")

elif mom.count("e") == 2 and dad.count("e") == 2:
    combos.append("e")

else:
    combos.append("E")
    combos.append("e")
    
for i in range(int(input())):
    child = True
    baby = list(input())
    for gene in baby:
        if gene not in combos:
            print("Not their baby!")
            child = False
            break
    if child == True:
        print("Possible baby.")
