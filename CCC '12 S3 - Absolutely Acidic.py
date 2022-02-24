import collections

readings = []

N = int(input())

for i in range(N):
    readings.append(int(input()))

frequencies = dict(collections.Counter(readings))


###Ordered by keys, not values
#Least to Greatest
readingsAndFrequenciesSToG = dict(collections.OrderedDict(sorted(frequencies.items(), reverse = True)))
listReadingsSToG = list(readingsAndFrequenciesSToG.keys())
listFrequenciesStoG = list(readingsAndFrequenciesSToG.values())

#print(readingsAndFrequenciesSToG)
#print(listReadingsSToG)
#print(listFrequenciesStoG)

#need to find max frequency, because keys are in order

maxFrequency = max(listFrequenciesStoG)

#check if max or min key is furthest


if listFrequenciesStoG.count(maxFrequency) == 1:

    maxReading = listReadingsSToG[listFrequenciesStoG.index(maxFrequency)]
    listFrequenciesStoG.remove(maxFrequency)
    listReadingsSToG.remove(maxReading)
    secondMaxFrequency = max(listFrequenciesStoG)
    if listFrequenciesStoG.count(secondMaxFrequency) == 1:

        print(abs(maxReading - listReadingsSToG[listFrequenciesStoG.index(secondMaxFrequency)]))
    
    else:
        diffs = []

        for i in range(listFrequenciesStoG.count(secondMaxFrequency)):
            num = listReadingsSToG[listFrequenciesStoG.index(secondMaxFrequency)]
            diffs.append(abs(maxReading - num))
            listFrequenciesStoG.remove(secondMaxFrequency)
            listReadingsSToG.remove(num)
        
        print(max(diffs))

else:
    maximums = []
    for i in range(listFrequenciesStoG.count(maxFrequency)):
        num = listReadingsSToG[listFrequenciesStoG.index(maxFrequency)]
        maximums.append(num)
        listFrequenciesStoG.remove(maxFrequency)
        listReadingsSToG.remove(num)

    maximum = max(maximums)
    minimum = min(maximums)
    print(abs(maximum-minimum))



