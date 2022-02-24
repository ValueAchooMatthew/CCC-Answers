k = int(input())

top = ("*")*k +("x")*k +("*")*k
middle = (" ")*k +("x")*k +("x")*k
bottom = ("*")*k +(" ")*k + ("*")*k

for i in range(k):
    print(top)

for j in range(k):
    print(middle)

for l in range(k):
    print(bottom)