a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())


stepCounterNikky = 0
positionN = 0

stepCounterByron = 0
positionB = 0
while stepCounterNikky < s:
    for i in range(a):
        if stepCounterNikky < s:
            positionN += 1
            stepCounterNikky += 1

    for i in range(b):
        if stepCounterNikky < s:
            positionN -= 1
            stepCounterNikky += 1


while stepCounterByron < s:
    for i in range(c):
        if stepCounterByron < s:
            positionB += 1
            stepCounterByron += 1

    for i in range(d):
        if stepCounterByron < s:
            positionB -= 1
            stepCounterByron += 1

if positionN > positionB:
    print("Nikky")

elif(positionN < positionB):
    print("Byron")

else: 
    print("Tied")


