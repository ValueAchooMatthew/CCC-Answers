import collections


lineOne = list(input())

while True:
    try:
        lineOne.remove(" ")
    except:
        break

lineTwo = list(input())

while True:
    try:
        lineTwo.remove(" ")
    except:
        break

lineOne = collections.Counter(lineOne)
lineOne = collections.OrderedDict(sorted(lineOne.items()))

lineTwo = collections.Counter(lineTwo)
lineTwo = collections.OrderedDict(sorted(lineTwo.items()))


if lineOne == lineTwo:
    print("Is an anagram.")


else:
    print("Is not an anagram.")