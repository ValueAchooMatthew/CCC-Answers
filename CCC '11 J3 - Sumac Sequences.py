sequence = []

start1 = int(input())
start2 = int(input())

sequence.append(start1)
sequence.append(start2)

counter = 0
 
while (sequence[counter]-sequence[counter +1]) <= sequence[counter +1]:
    sequence.append(sequence[counter]-sequence[counter +1])
    counter += 1

print(len(sequence)+1)