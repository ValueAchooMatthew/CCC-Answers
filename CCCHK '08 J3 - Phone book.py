from collections import Counter


n = int(input())

names = []
numbers = []
dialed = []
frequencies = []
counts = []

for i in range(n):
    pb = input().split()
    names.append(pb[0])
    numbers.append(int(pb[1]))

o = int(input())

for j in range(o):
    dialed.append(int(input()))


counts = Counter(dialed)

calls = list(counts.keys())
nums = list(counts.values())

maxnums = nums.count(max(nums))

fn = []

for l in range(maxnums):
    fn.append(calls[nums.index(max(nums))])
    nums[nums.index(max(nums))] = 0

final = min(fn)


print(names[numbers.index(final)])