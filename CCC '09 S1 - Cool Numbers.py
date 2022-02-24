from math import ceil, floor
a =float(input())
b = float(input())

cubes = []
counter = 0


for i in range(ceil(a**(1/3)), floor(round(b**(1/3)))+1):
    cubes.append(float(i**3))

for j in range(ceil(a**(1/2)), floor(b**(1/2))+1):
    if float(j**2) in cubes:
        counter += 1



print(counter)