Tests = int(input())

for i in range(Tests):
    N = int(input())
    cars = []
    side = []
    for i in range(N):
        cars.append(int(input()))

    water = 1
    checkerCars = []
    checkerSide = []
    while True:

        if len(cars) == 0 and len(side) == 0:
            print("Y")
            break
        
        else:

            if len(cars) >= 1 and cars[-1] == water:
                cars.pop(-1)
                water +=1
            
            elif len(side) >= 1 and side[-1] == water:
                side.pop(-1)
                water +=1
            
            elif len(cars) >=1:
                    side.append(cars[-1])
                    cars.pop(-1)
    
            else:
                print("N")
                break




