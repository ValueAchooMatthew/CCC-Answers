import sys

command = list(sys.stdin.readline())

command.pop()

block = [1, 2,
         3, 4]


for i in range(len(command)):
    if command[i] == "H":
        block[0], block[1], block[2], block[3] = block[2], block[3], block[0], block[1]
    else:
        block[0], block[1], block[2], block[3] = block[1], block[0], block[3], block[2]


print(block[0], block[1])
print(block[2], block[3])