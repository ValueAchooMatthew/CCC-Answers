speedLimit = int(input())
carSpeed = int(input())

diff = carSpeed - speedLimit

if diff <= 0:
    print("Congratulations, you are within the speed limit!")
elif diff > 1 and diff <21:
    print("You are speeding and your fine is $100.") 
elif diff >=31:
    print("You are speeding and your fine is $500.")
else:
    print("You are speeding and your fine is $270.")
