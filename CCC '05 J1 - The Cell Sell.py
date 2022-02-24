daytime = int(input())
evening = int(input())
weekend = int(input())

daytimeA = daytime - 100

daytimeB = daytime - 250

planA = max(0, daytimeA)*.25 + evening*.15 + weekend*.20

planB = max(0, daytimeB)*.45 + evening*.35 + weekend*.25

print("Plan A costs %.2f" %planA)
print("Plan B costs %.2f" %planB)

if planA == planB:
    print("Plan A and B are the same price.")

elif planA > planB:
    print("Plan B is cheapest.")

else:
    print("Plan A is cheapest.")


