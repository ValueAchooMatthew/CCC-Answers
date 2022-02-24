weight, height = float(input()), float(input())

BMI = (weight)/(height**height)

if BMI < 18.5:
    print("Underweight")

elif(BMI > 25):
    print("Overweight")

else:
    print("Normal weight")