n = int(input())
heights = list(map(float, input().split()))
bases = list(map(float, input().split()))

area = 0

for i in range(n):
    area += (heights[i] + heights[i+1])/2 * bases[i]

print(area)