N = int(input())

times = []

colin = {}

for i in range(N):
    observation = list(map(int, input().split()))
    time, position = observation
    times.append(observation[0])
    colin[time] = position

times.sort()

speeds = []

for i in range(N-1):
    speeds.append(abs(colin[times[i+1]] - colin[times[i]])/(times[i+1] - times[i]))

print(float(max(speeds)))