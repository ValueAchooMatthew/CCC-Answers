L = int(input())

animals = []
n = int(input())
animals.append(list(map(int, input().split())))

for i in range(n-1):
    animal = list(map(int, input().split()))
    for boundary in animals:
        if animal[0] < boundary[-1] and animal[1] > boundary[-1]:
            intermed = boundary[0]
            
            animals.append(intermed)
            animals.remove(boundary)

print(animals)

# counter = 0
# counters = []
# for k in range(L):
#     counter += 1
    
#     for boundary in animals:
#         if k >= boundary[-1] or k < boundary[0]:
#             pass
        
#         else:
#             counter = 0
#             break

#     counters.append(counter)    

# print(max(counters))