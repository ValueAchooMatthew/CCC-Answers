import collections


yodellers, competitions = list(map(int, input().split()))

scores = {}

brackets = []

for i in range(1, yodellers+1):
    scores[i] = 0



for i in range(competitions):
    yodels = list(map(int, input().split()))
    for j in range(1, yodellers+1):
        scores[j] += yodels[j-1]
    
    brackets.append(sorted(scores.values()))





print(scores.keys max(scores.values()))


print(scores)
print(brackets)