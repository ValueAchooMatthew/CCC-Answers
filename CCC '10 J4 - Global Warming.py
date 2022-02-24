import itertools as it

while True:
    length, *nums = list(map(int, input().split()))
    if length == 0:
        break
    elif length == 1:
        print(0)

    else: 
    
        diffs = []
        for i in range(1, length):
            diffs.append(nums[i] - nums[i-1])

        solved = False
        suppArr = []

        while not solved:
            suppArr.append(diffs.pop(0))
            solved = True
            for x, y in zip(diffs, it.cycle(suppArr)):
                if not x == y:
                    solved = False
                    break
        print(len(suppArr))
