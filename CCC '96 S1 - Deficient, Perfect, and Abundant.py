for i in range(int(input())):
    number = int(input())
    divisors = []
    for j in range(1, number//2+1):
        if number % j == 0:
            divisors.append(j)

    if sum(divisors) == number:
        print(number, "is a perfect number.")
    elif sum(divisors) > number:
        print(number, "is an abundant number.")
    else:
        print(number, "is a deficient number.")