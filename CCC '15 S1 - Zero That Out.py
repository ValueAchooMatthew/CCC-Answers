K = int(input())

amount = []

for i in range(K):
    command = int(input())
    if command == 0:
        amount = amount.pop()
    else:
        amount.append(command)

print(sum(amount))