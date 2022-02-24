N = int(input())

tCounter = 0
sCounter = 0

for i in range(N):
    sentence = input()
    sentence = sentence.lower()
    tCounter += sentence.count("t")
    sCounter += sentence.count("s")
    

if tCounter > sCounter:
    print("English")

else:
    print("French")

