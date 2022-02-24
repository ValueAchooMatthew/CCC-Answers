start = int(input())
end = int(input())

total = 0
divisors = 0
for i in range(start, end +1):
    divisors = 0
    for j in range(1, i+1):
        if i % j == 0:
            divisors += 1 
        else:
            pass
    if divisors == 4:
        total += 1
    else:
        pass

print("The number of RSA numbers between", str(start), "and", str(end), "is", total)
